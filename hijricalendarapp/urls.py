from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path("month/", views.hijri_month, name="month"),
]