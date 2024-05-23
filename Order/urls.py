from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('vieworders/', OrderView.as_view()),
    path('orders/',OrderCreate.as_view()),
]