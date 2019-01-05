"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from booking.views import BookingDelete, History

# TODO: decorate the class view with login_required here. see:
# https://docs.djangoproject.com/en/2.1/topics/class-based-views/intro/#decorating-class-based-views
urlpatterns = [
	path('book_seat/<int:screening_id>/', views.book_seat, name='book_seats'),
	path('manage_bookings/', BookingDelete.as_view(), name='manage_bookings'),
	path('booking_history/', History.as_view(), name='booking_history')
]
