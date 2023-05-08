from django.db import models
from django.urls import reverse, is_valid_path
from django.core.exceptions import ValidationError
# from django_jalali.db import models as jmodels

class Event(models.Model):
    """An Event on the Calendar"""

    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, help_text="Description", max_length=500)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)