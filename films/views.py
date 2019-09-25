from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from cinema.cinema_logger import logger
from .models import Screening
from .forms import ScreeningDateForm


@login_required
def date_choice(request):
	"""Show the page to filter screenings by specific date. The form does the work."""
	form = ScreeningDateForm
	return render(request, 'films/date_choice.html', {'form': form})


@login_required
def screening_choice(request):
	"""Show future screenings or (if POST) show for a chosen date"""
	screenings = Screening.objects.filter(date_time__gt=timezone.now()).order_by('date_time')
	if request.method == 'POST':
		chosen_date = request.POST.__getitem__('date_choice')
		chosen_date = datetime.strptime(chosen_date, '%Y-%m-%d')
		logger.info(chosen_date)
		screenings = Screening.objects.filter(date_time__date=chosen_date).order_by('date_time')
		for screening in screenings:
			logger.info(screening.film.title)
	return render(request, 'films/screening_choice.html', {'screenings': screenings})
