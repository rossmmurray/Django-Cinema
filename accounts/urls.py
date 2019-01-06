from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update_profile/', login_required(views.UpdateProfile.as_view()), name='update_profile')
]
