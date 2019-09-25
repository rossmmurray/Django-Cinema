from django.urls import reverse
from accounts.tests import UserSetUp


class BookingViewTest(UserSetUp):

	def test_good_response(self):
		"""Get a 404 back from the view when there are no screenings"""
		response = self.normal_user.get(reverse('book_seats', args=[1]))
		self.assertEqual(response.status_code, 404)
