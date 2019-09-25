from django.utils.timezone import now
from django import forms
from .models import Screening


class ScreeningDateForm(forms.Form):
	"""Form so user can filter screenings by date."""

	# get screening dates in the future
	screenings = Screening.objects.filter(date_time__gt=now())
	screenings = screenings.distinct('date_time__date')
	# screenings_list = list(screenings.values_list('date_time__date'))

	# convert queryset into right format for ChoiceField
	date_list = []
	for screening in screenings:
		date_list.append((screening.date_time.date(), screening.date_time.date()))

	# show date choice on form
	date_choice = forms.ChoiceField(choices=date_list, widget=forms.Select(attrs={'class': 'wideInput'}))
