from django.urls import path
from srinu.views import *

app_name='srinu'

urlpatterns=[
    path('bharathi/',bharathi,name='bharathi'),
    path('janith/',janith,name='janith'),
]