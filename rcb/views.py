from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kholi(request):
    return render(request,'kholi.html')
def kholi2(request):
    return HttpResponse('HIII Kholi')
