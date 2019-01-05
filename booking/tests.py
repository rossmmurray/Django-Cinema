from django.test import TestCase
from django.urls import reverse


class BookingViewTest(TestCase):

	def test_good_response(self):
		# TODO: it is being redirected because the user ain't logged in
		"""Get a 302 back from the view when the user isn't logged in"""
		response = self.client.get(reverse('book_seats', args=[1289677]))
		self.assertEqual(response.status_code, 302)
