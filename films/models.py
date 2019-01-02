from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils import timezone
from cinema.cinema_logger import logger
from film_services import screening_overlap


class Film(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return f'{self.description[:50]}...'


class Screening(models.Model):
	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	date_time = models.DateTimeField()

	def __str__(self):
		return f'{self.film.title} at {self.date_time: %I:%M %p} on {self.date_time: %d/%m/%y }'

	def get_date(self):
		return self.date_time.date()

	def clean(self):
		"""Validation: automatically run when screening objects are created"""

		# screenings must be in the future
		if self.date_time < timezone.now():
			raise ValidationError('Screenings must be in the future.')

		# screenings cannot overlap
		overlapping_screenings = screening_overlap(self.date_time, Screening.objects.all())
		if overlapping_screenings:
			error_message = f"The screening clashed with the existing screening: {overlapping_screenings[0]}. The " \
							f"screening wasn't added."
			logger.warning(error_message)
			raise ValidationError(error_message)
		else:
			logger.info("There are no clashes.")


class Seat(models.Model):
	seat_no = models.IntegerField()
	screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
	available = models.BooleanField()

	def __str__(self):
		return f'Seat {self.seat_no} for {self.screening.__str__()}'


@receiver(post_save, sender=Screening)
def create_seats(sender, instance, created, *args, **kwargs):
	"""Create all seats with Availability=True on creation of a screening."""
	if created:
		number_of_seats = 36
		for i in range(number_of_seats):
			new_seat = Seat(seat_no=i+1, screening=instance, available=True)
			new_seat.save()
			logger.info(new_seat)
