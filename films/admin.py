from django.contrib import admin
from films.models import Film, Screening, Seat


admin.site.register(Film)
admin.site.register(Screening)
# admin.site.register(Seat)