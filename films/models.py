from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
		for i in range(36):
			new_seat = Seat(seat_no=i+1, screening_id=instance.id, available=True)
			new_seat.save()
			print(new_seat)
