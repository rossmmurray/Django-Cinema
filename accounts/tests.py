from django.test import TestCase
from django.urls import reverse
from django.test import Client


class AccountViewTests(TestCase):

	def test_good_response(self):
		"""Get a 200 back from the view"""
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



