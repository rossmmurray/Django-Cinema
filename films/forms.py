from django import forms
from .models import Screening
from django.utils.timezone import now


class ScreeningDateForm(forms.Form):

	# get screening dates in the future
	screenings = Screening.objects.filter(date_time__gt=now())
	screenings = screenings.distinct('date_time__date')
	screenings_list = list(screenings.values_list('date_time__date'))

	# convert queryset into right format for ChoiceField
	date_list = []
	for key, value_tuple in enumerate(screenings_list):
		date_list.append((value_tuple[0], value_tuple[0]))

	date_choice = forms.ChoiceField(choices=date_list, widget=forms.Select(attrs={'class': 'wideInput'}))
