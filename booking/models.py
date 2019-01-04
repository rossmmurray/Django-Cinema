from django.db import models
from films.models import Seat, Screening
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cinema.cinema_logger import logger
from django.utils import timezone
from django.core.exceptions import ValidationError


class Booking(models.Model):
	seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"Booking by {self.user} of seat {self.seat.seat_no} for {self.seat.screening}."

	def clean(self):
		"""Validation: prevent creation/modification of past bookings. This does not prevent deletions!"""
		screening_start = self.seat.screening.date_time
		if screening_start < timezone.now():
			print('raising the error!')
			raise ValidationError('You cannot modify or create past bookings.')

# @receiver(post_save, sender=Seat)
# def create_seats(sender, instance, created, update_fields, *args, **kwargs):
# 	"""Create all seats with Availability=True on creation of a screening."""
# 	# if created:
# 	# 	number_of_seats = 36
# 	# 	for i in range(number_of_seats):
# 	# 		new_seat = Seat(seat_no=i+1, screening=instance, available=True)
# 	# 		new_seat.save()
# 	# 		logger.info(new_seat)
# 	print("message received", update_fields)
