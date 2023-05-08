from django.shortcuts import render
from django.urls import re_path, path
from .views import index, Calendar, CalendarView

urlpatterns = [
    # re_path(r'^index/$', index, name='index'),
    re_path(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    #re_path('', CalendarView.as_view(), name='calendar')
]