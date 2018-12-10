from django import forms
from .models import Screening
from datetime import date


class ScreeningDateForm(forms.Form):
	screenings = Screening.objects.distinct('date_time__date')
	screenings_list = list(screenings.values_list('date_time__date'))

	# print('\nthis is a list:\n', screenings_list)

	# covert querset into right format for ChoiceField
	date_list = []
	for key, value_tuple in enumerate(screenings_list):
		date_list.append((key, value_tuple[0]))


	# print(date_list)

	# screenings = screenings.values_list('date_time__date')
	# dates = screenings
	# date_choice = forms.ModelChoiceField(queryset=screenings)
	# temp = [(1, date(2018, 1, 1)), (2, date(2018, 1, 1))]
	date_choice = forms.ChoiceField(choices=date_list)
