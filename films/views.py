from django.shortcuts import render
from .models import Film, Screening


def index(request):
	films = Film.objects
	screenings = Screening.objects.all()
	screening_dates = []
	for screening in screenings:
		screening_dates.append(screening.get_date())
	# print(screening_dates)
	screening_dates = set(screening_dates)
	# print(type(screening_dates.pop()))
	return render(request, 'films/home.html', {'films': films, 'screening_dates': screening_dates})


def screening_choice(request):
	films = Film.objects
	screenings = Screening.objects.all()
	return render(request, 'films/screening_choice.html', {'films': films, 'screenings': screenings})


# def home(request):
# 	jobs = Job.objects
# 	return render(request, 'jobs/home.html', {'jobs': jobs})