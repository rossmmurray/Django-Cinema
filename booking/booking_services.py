# helper functions for booking app
from films.models import Seat
from django.db.models.query import QuerySet
from typing import Iterable, List


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


def make_booking(selected_seat: Seat):
	"""Make seat unavailable to make booking or show error"""
	if selected_seat.available:
		selected_seat.available = False
		selected_seat.save()
		return True
	else:
		return False
