from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update_profile/', login_required(views.UpdateProfile.as_view()), name='update_profile')
]
