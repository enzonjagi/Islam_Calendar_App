from django.db import models
from django.urls import reverse, is_valid_path
from django.core.exceptions import ValidationError
# from django_jalali.db import models as jmodels

class Month(models.Model):
    """A model for a Hijri Month on the DB"""

    hijri_month = models.CharField(max_length=100, blank=True, null=True)
    hijri_year = models.CharField(max_length=100, blank=True, null=True)
    hijri_day = models.CharField(max_length=100, blank=True, null=True)
    gregorian_month = models.CharField(max_length=100, blank=True, null=True)
    gregorian_day = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name