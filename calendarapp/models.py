from django.db import models

class Person(models.Model):
    """A model to Create a Person"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)