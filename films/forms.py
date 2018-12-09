from django import forms


class ScreeningDateForm(forms.Form):
	date_choice = forms.CharField(label="Select date")
