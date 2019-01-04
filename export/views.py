from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv
from export.export_services import get_cinema_data
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def csv_data_export(request):
	"""Download csv file to local system."""

	# preparing CSV file
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="AllCinemaData.csv"'
	writer = csv.writer(response)

	# adding relevant cinema data to CSV
	cinema_data = get_cinema_data()
	for row in cinema_data:
		writer.writerow(row)

	# automatically downloads for user
	return response
