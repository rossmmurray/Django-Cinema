from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User


class LoginSignupTests(TestCase):
	"""Test the login and signup parts of accounts view"""

	def test_good_response(self):
		"""Get a 200 back from signup and login accounts views"""
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code, 200)
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code, 200)

	def test_normal_signup(self):
		"""Test normal signup"""
		user_details = {
			'username': "test1",
			'password': "testing123",
			'password-confirmation': "testing123"
		}
		response = self.client.post(reverse('signup'), user_details)
		self.assertEqual(response.status_code, 302)

	def test_existing_username_signup(self):
		"""Try signup with same username twice - should return error"""
		user_details = {
			'username': "test2",
			'password': "testing1234",
			'password-confirmation': "testing1234"
		}
		self.client.post(reverse('signup'), user_details)
		response = self.client.post(reverse('signup'), user_details)
		self.assertEqual(response.context['error'], 'Username already exists')


class UserSetUp(TestCase):
	"""Login and test profile updates"""

	def setUp(self):
		self.user_model = User.objects.create_user('john', password='test_password')
		self.normal_user = Client()
		self.normal_user.login(username='john', password='test_password')


class UpdateProfile(UserSetUp):

	def test_update_profile_page_get(self):
		"""get to update_profile page as logged in user"""
		response = self.normal_user.get(reverse('update_profile'))
		self.assertEqual(response.status_code, 200)

	def test_email_validation(self):
		"""Test updating to valid and invalid emails"""
		email_tests_and_results = {
			'testing2@gmail.com': 'testing2@gmail.com',
			'testing.com': '',
			'blah': '',
			'ross@yahoo.com': 'ross@yahoo.com'
		}

		for email, result in email_tests_and_results.items():
			self.normal_user.post(reverse('update_profile'), {'email': email})
			self.user_model.refresh_from_db()
			self.assertEqual(self.user_model.email, result)

			# blank out previous email
			self.user_model.email = ''
			self.user_model.save()









