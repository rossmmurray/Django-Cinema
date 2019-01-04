from films.models import Screening, Seat


def get_cinema_data():
	"""Prepare film, screening and seat availability data for CSV output."""

	# field headings
	cinema_data = [['Title', 'Date', 'Time', 'Available', 'Booked']]

	# get data values
	screenings = Screening.objects.all()
	for screening in screenings:
		seat_data = get_seat_info(screening)
		cinema_data.append([
			screening.film.title,
			f'{screening.date_time.date(): %d/%m/%y}',
			f'{screening.date_time.time(): %I:%M %p}',
			seat_data['available'],
			seat_data['booked']])

	return cinema_data


def get_seat_info(screening: Screening) -> dict:
	"""Get information on seat availability given a screening."""
	seat_info = {}
	seats = Seat.objects.filter(screening=screening)
	seat_info['total'] = seats.count()
	seat_info['available'] = seats.filter(available=True).count()
	seat_info['booked'] = seats.filter(available=False).count()

	return seat_info


