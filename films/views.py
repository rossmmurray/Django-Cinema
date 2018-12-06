from django.shortcuts import render
from .models import Film


def index(request):
	films = Film.objects
	return render(request, 'films/home.html', {'films': films})


# def home(request):
# 	jobs = Job.objects
# 	return render(request, 'jobs/home.html', {'jobs': jobs})