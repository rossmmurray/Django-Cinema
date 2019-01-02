from django.shortcuts import render, get_object_or_404
from films.models import Screening, Seat
from .booking_services import create_seat_layout, make_booking


def book_seat(request, screening_id):
	"""Booking page view"""

	# set up initial booking variables to pass to template
	info = ''
	booked = None

	# if post request, get user seat selection
	if request.method == 'POST':

		# get seat from model
		selected_seat_id = request.POST.__getitem__('selected_seat')
		selected_seat = Seat.objects.get(id=selected_seat_id)

		# make seat unavailable to make booking or show error
		booked = make_booking(selected_seat, request)
		if booked:
			info = f'Success! Booked {selected_seat}'
		else:
			info = f'Sorry, seat not available'

	# get all seat info from url
	screening = get_object_or_404(Screening, pk=screening_id)
	seats = Seat.objects.filter(screening_id=screening).order_by('seat_no')

	# get seat layout (structure to represent rows / columns)
	seat_columns = 6
	seat_layout = create_seat_layout(seats, seat_columns)

	return render(request, 'book_seat.html', {
		'seat_layout': seat_layout,
		'booked': booked,
		'info': info})
