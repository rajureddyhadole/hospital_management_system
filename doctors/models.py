from django.db import models

# Create your models here.

class Doctor(models.Model):
  name = models.CharField(max_length=200)
  specification = models.CharField(max_length=200)