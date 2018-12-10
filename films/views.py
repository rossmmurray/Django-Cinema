from django.shortcuts import render
from .models import Film, Screening
from datetime import date
from .forms import ScreeningDateForm
from django.http import HttpResponseRedirect


def date_choice(request):
	screenings = Screening.objects.distinct('date_time__date')
	# print(screenings)
	if request.method == 'POST':
		form = ScreeningDateForm(request.POST)
		print('\n this is a form\n', form)
		if form.is_valid():
			return HttpResponseRedirect('accounts/login.html')
	else:
		form = ScreeningDateForm

	return render(request, 'films/date_choice.html', {'form': form})

"""

	# if get, show dates with films
	if request.method == 'GET':
		films = Film.objects
		screenings = Screening.objects.all()
		screening_dates = []
		for screening in screenings:
			# print(screening.get_date())
			screening_dates.append(screening.get_date())
		screening_dates = set(screening_dates)
		print(screening_dates)
		form = ScreeningDateForm()
		return render(request, 'films/date_choice.html', {'films': films, 'screening_dates': screening_dates, 'form': form})

	# if post, send screenings to screening_choice view
	else:
		chosen_date = request.POST['screening_date']
		print(type(chosen_date))
		# TODO: find relevant screenings then
		screenings = Screening.objects

		# screenings_on_date = screenings.all().filter(date_time__date=chosen_date)
		films = Film.objects
		screenings = Screening.objects
		return render(request, 'films/screening_choice.html', {'films': films, 'screenings': screenings})
"""

def screening_choice(request):
	films = Film.objects
	screenings = Screening.objects.all()
	return render(request, 'films/screening_choice.html', {'films': films, 'screenings': screenings})

