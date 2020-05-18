from django.urls import path
from . import views as user_views

app_name = 'user'

urlpatterns = [
    path('', user_views.homepage),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile-edit/', user_views.profile_edit, name='profile'),
]
