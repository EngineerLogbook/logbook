from django.urls import path
from . import views as user_views

urlpatterns = [
    path('', user_views.landingpage, name='landing-page'),
    path('home/', user_views.homepage, name='user-home'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('newlog/',user_views.newlog, name='newlog'),
    path('profile-edit/', user_views.profile_edit, name='profile-edit'),
]

