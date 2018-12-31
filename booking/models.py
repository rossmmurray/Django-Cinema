from django.db import models
from films.models import Seat
from django.contrib.auth.models import User


class Booking(models.Model):
	seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cancelled = models.BooleanField()
