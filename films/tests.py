from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
	def test_good_response(self):
		"""Get a 200 back from the view"""
		response = self.client.get(reverse('screening_choice'))
		self.assertEqual(response.status_code, 200)
