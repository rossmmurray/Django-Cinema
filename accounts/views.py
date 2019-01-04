from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.core.validators import validate_email
from django.contrib.messages.views import SuccessMessageMixin


def signup(request):
	"""Page for user to create login"""
	if request.method == 'POST':

		# check passwords aren't the same
		if request.POST['password'] != request.POST['password-confirmation']:
			return render(request, 'accounts/signup.html', {'error': 'Your passwords must match'})

		# check if username already exists
		try:
			user = User.objects.get(username=request.POST['username'])
			return render(request, 'accounts/signup.html', {'error': 'Username already exists'})

		# create user if it doesn't work
		except User.DoesNotExist:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
				print("trying to sign up")
				auth.login(request, user)
				return redirect('date_choice')
			# if user enters empty string
			except ValueError:
				return render(request, 'accounts/signup.html', {'error': 'You must enter a reasonable username. No empty strings.'})

	# user wants to come to signup page
	else:
		return render(request, 'accounts/signup.html')


def login(request):
	"""Login page."""
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('date_choice')
		else:
			return render(request, 'accounts/login.html', {'error': 'username or password is wrong'})
	else:
		return render(request, 'accounts/login.html')


def logout(request):
	"""Log out current user."""
	if request.method == 'POST':
		auth.logout(request)
		return redirect('login')

# TODO: make so that this is login required
# @login_required
# def update_profile(request):
# 	"""Let user update profile."""
# 	return render(request, 'accounts/user_form.html')


class UpdateProfile(SuccessMessageMixin, UpdateView):
	model = User
	fields = ['email', 'first_name', 'last_name']
	template_name = 'accounts/user_form.html'
	pk_url_kwarg = 'user_id'
	success_message = 'Details updated!'
	# success_url = reverse_lazy('update_profile')
	# the template is user_form.html

	def get_object(self, queryset=None):
		return self.request.user

	def get_success_url(self):
		return reverse_lazy('update_profile')



