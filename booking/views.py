from django.shortcuts import render, get_object_or_404
from films.models import Screening, Seat


# Create your views here.
def book_seat(request, screening_id):
	screening = get_object_or_404(Screening, pk=screening_id)
	seats = Seat.objects.filter(screening_id=screening).order_by('seat_no')
	seat_columns = 6
	current_column=0
	seat_layout = []
	seat_row = []
	appearance = {}

	for seat in seats:

		# determine appearance (bootstrap class) for seat
		if seat.available == True:
			appearance[seat.seat_no] = 'info'
		else:
			appearance[seat.seat_no] = 'outline-danger'


		# put seat into 2D-list to represent rows and columns
		seat_row.append(seat)
		current_column += 1
		if current_column == seat_columns:
			seat_layout.append(seat_row)
			seat_row = []
			current_column = 0


	return render(request, 'book_seat.html', {'seat_layout': seat_layout})