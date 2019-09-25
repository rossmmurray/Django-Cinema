from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from films.models import Seat


class Booking(models.Model):
	"""Holds booking records"""
	seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"Booking by {self.user} of seat {self.seat.seat_no} for {self.seat.screening}"

	def clean(self):
		"""Validation: prevent creation/modification of past bookings. This does not prevent deletions!"""
		screening_start = self.seat.screening.date_time
		if screening_start < timezone.now():
			print('raising the error!')
			raise ValidationError('You cannot modify or create past bookings.')


class BookingHistory(models.Model):
	"""Holds booking creation and deletion actions"""
	action = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	action_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.action} at {self.action_time:%I:%M %p} on {self.action_time:%d/%m/%y}'"
