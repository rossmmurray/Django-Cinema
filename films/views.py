from django.shortcuts import render
from .models import Film, Screening
from datetime import datetime
from .forms import ScreeningDateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cinema.cinema_logger import logger
# TODO: get rid of unused package imports


@login_required
def date_choice(request):
	# TODO: get rid or massive docstring comment.
	'''
	screenings = Screening.objects.distinct('date_time__date')


	print(screenings)
	if request.method == 'POST':
		pass
		print('\n this is a form\n')
		form = ScreeningDateForm(request.POST)
		print('\n this is a form\n', form)
		if form.is_valid():
			pass
			# return HttpResponseRedirect('login.html')
	else:
		print('\n blah \n')
		form = ScreeningDateForm
	'''

	# TODO: get rid of this stupid form and just put the logic in the view
	form = ScreeningDateForm
	return render(request, 'films/date_choice.html', {'form': form})


@login_required
def screening_choice(request):
	# TODO: put two different returns for post and get (render / redirect)
	# TODO: find out why the date page appears when using ?next post param for any page
	films = Film.objects
	screenings = Screening.objects.all()
	if request.method == 'POST':
		chosen_date = request.POST.__getitem__('date_choice')
		chosen_date = datetime.strptime(chosen_date, '%Y-%m-%d')
		print(chosen_date)
		screenings = Screening.objects.filter(date_time__date=chosen_date)
		for screening in screenings:
			logger.info(screening.film.title)
	return render(request, 'films/screening_choice.html', {'films': films, 'screenings': screenings})

