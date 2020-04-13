from django.db import models
from django.conf import settings

# Create your models here.

class Year(models.Model):
    year = models.CharField(primary_key=True, max_length=300)
    def __str__(self):
        return '%s' % self.year

class Data(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    status = models.CharField(max_length=100)
    def __str__(self):
        return '%s' % self.name