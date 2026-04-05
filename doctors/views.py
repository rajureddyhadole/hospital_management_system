from django.shortcuts import render
from .models import Doctor
# Create your views here.

def doctors_list(request):
  doctors = Doctor.objects.all()

  return render(request, 'doctor_list.html', {'doctors': doctors})