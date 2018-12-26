from django.shortcuts import render, get_object_or_404
from films.models import Screening


# Create your views here.
def book_seat(request, screening_id):
	screening = get_object_or_404(Screening, pk=screening_id)
	return render(request, 'book_seat.html', {'screening': screening})