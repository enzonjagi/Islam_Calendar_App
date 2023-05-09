from __future__ import unicode_literals
from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    """The admin view for the Events users create"""

    list_display = ['title', 'Description', 'end_time', 'start_time']

admin.site.register(Event)