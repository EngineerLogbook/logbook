from django.urls import path
from . import views as user_views

urlpatterns = [
    path('', user_views.homepage, name='home'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('createlog/', user_views.makelog, name='createlog'),
    path('markdownguide/',user_views.viewguide, name='guide'),
]
