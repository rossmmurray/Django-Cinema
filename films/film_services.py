from datetime import timedelta, datetime
from django.db.models.query import QuerySet
from cinema.cinema_logger import logger


def screening_overlap(start_time: datetime, all_screenings: QuerySet):
	"""Return films that could clash with another"""

	# get time window
	screening_start_time = start_time - timedelta(hours=1)
	screening_end_time = start_time + timedelta(hours=1)

	# search for screenings between time
	clashing_films = all_screenings.filter(date_time__range=(screening_start_time, screening_end_time))

	# make into list so that empty structure resolves to boolean False
	# clashing_films = list(clashing_films)

	logger.info(f'clashing films are: {clashing_films}')

	return clashing_films
