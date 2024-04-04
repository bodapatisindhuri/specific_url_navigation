from django.contrib import admin
from django.urls import path
from guru.views import *

app_name='guru'

urlpatterns=[
    path('mani/',mani,name='mani'),
    path('sindhu/',sindhu,name='sindhu'),
]