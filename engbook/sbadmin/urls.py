from django.urls import path
from sbadmin.views import *

urlpatterns = [
    path('base/', baseview, name='sbadmin-base')
]
