from django.db import models

# Create your models here.

class Patient(models.Model):
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=15)
  email = models.EmailField()