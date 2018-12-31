from django.test import TestCase
from django.urls import reverse


class BookingViewTest(TestCase):

	def test_good_response(self):
		"""Get a 404 back from the view when a random number is chosen"""
		response = self.client.get(reverse('book_seats', args=[12]))
		self.assertEqual(response.status_code, 404)