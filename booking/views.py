from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from booking.models import Booking, BookingHistory
from films.models import Screening, Seat
from export.export_services import get_seat_info
from .booking_services import create_seat_layout, make_booking, delete_booking


@login_required
def book_seat(request, screening_id):
	"""Display booking page. Get and Layout all seats"""

	# initialise booking variables to pass to template
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

	# get information on total number of available/booked seats
	seat_info = get_seat_info(screening)

	return render(request, 'booking/book_seat.html', {
		'seat_layout': seat_layout,
		'booked': booked,
		'info': info,
		'available_seats': seat_info['available'],
		'booked_seats': seat_info['booked']})


class History(ListView):
	"""Simple page to show booking history."""

	def get_queryset(self):
		"""Get booking history for user."""
		return BookingHistory.objects.filter(user=self.request.user)


class BookingDelete(ListView):
	"""Class based view used so that the django generic view 'ListView' can be taken advantage of. N.B a get method is
	not necessary since it is provided for free by the generic view. """

	def get_queryset(self):
		"""Define bookings to show i.e. bookings linked to current user"""
		return Booking.objects.filter(user=self.request.user)

	def post(self, request):
		"""Actions to perform on post request (booking deletion)."""

		# get booking id from user
		selected_booking_id = request.POST.__getitem__('booking')
		selected_booking = Booking.objects.get(id=selected_booking_id)

		# delete booking if it's for the past
		delete_flag = delete_booking(selected_booking, self.request)
		deletion_message = 'Success! Booking deleted.' if delete_flag else 'Past bookings cannot be deleted.'

		# get remaining user_bookings
		user_bookings = Booking.objects.filter(user=self.request.user)

		return render(request, 'booking/booking_list.html', {
			'booking_list': user_bookings,
			'deletion_message': deletion_message,
			'delete_flag': delete_flag})
