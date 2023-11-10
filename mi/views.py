from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bumra(request):
    return render(request,'mi.html')
def bumra2(request):
    return HttpResponse('Hiiii bumra')