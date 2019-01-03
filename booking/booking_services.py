""" Helper functions for booking app"""

from films.models import Seat
from django.db.models.query import QuerySet
from typing import Iterable, List
from booking.models import Booking
from django.http.request import HttpRequest


def create_seat_layout(seats: QuerySet, seat_columns: int) -> List:
	"""Create structure to represent the layout (rows/columns) of seats."""
	current_column = 0
	seat_layout = []
	seat_row = []
	for seat in seats:
		seat_row.append(seat)
		current_column += 1
		if current_column == seat_columns:
			seat_layout.append(seat_row)
			seat_row = []
			current_column = 0
	return seat_layout


def make_booking(selected_seat: Seat, request: HttpRequest):
	"""Create booking record and make seat unavailable"""

	if selected_seat.available:

		# make seat unavailable
		selected_seat.available = False
		selected_seat.save()

		# create new booking record
		new_booking = Booking(seat=selected_seat, user=request.user)
		new_booking.save()
		print("Created new booking:", new_booking)

		return True
	else:
		return False


def delete_booking(booking: Booking):
	"""Delete booking and make seat available again"""

	# delete booking record
	booking.delete()

	# free up the seat
	re_available_seat = Seat.objects.get(id=booking.seat_id)
	re_available_seat.available = True
	re_available_seat.save()

	return booking
