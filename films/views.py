from django.shortcuts import render
from .models import Film, Screening
from datetime import datetime
from .forms import ScreeningDateForm
from django.http import HttpResponseRedirect


def date_choice(request):
	print('\nbegin date choice\n')
	screenings = Screening.objects.distinct('date_time__date')
	# print(screenings)
	if request.method == 'POST':
		print('\n this is a form\n')
		form = ScreeningDateForm(request.POST)
		print('\n this is a form\n', form)
		if form.is_valid():
			pass
			# return HttpResponseRedirect('login.html')
	else:
		print('\n blah \n')
		form = ScreeningDateForm

	print('\n doing this return\n')
	return render(request, 'films/date_choice.html', {'form': form})


def screening_choice(request):
	films = Film.objects
	screenings = Screening.objects.all()
	if request.method == 'POST':
		print('\nthis is a post\n')
		chosen_date = request.POST.__getitem__('date_choice')
		chosen_date = datetime.strptime(chosen_date, '%Y-%m-%d')
		print(chosen_date)
	return render(request, 'films/screening_choice.html', {'films': films, 'screenings': screenings})

