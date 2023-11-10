"""
URL configuration for project4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from csk.views import *
from rcb.views import * 
from mi.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('msd/',msd,name='msd'),
    path('msd2/',msd2,name='msd2'),
    path('kholi/',kholi,name='kholi'),
    path('kholi2/',kholi2,name='kholi2'),
    path('bumra/',bumra,name='bumra'),
    path('bumra2/',bumra2,name='bumra2'),
]
