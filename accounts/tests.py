from django.test import TestCase
from django.urls import reverse


class AccountViewTests(TestCase):
	def test_good_response(self):
		"""Get a 200 back from the view"""
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code, 200)
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code, 200)
