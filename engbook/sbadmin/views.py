from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def baseview(request):
    return render(request, 'sbadmin/base.html')