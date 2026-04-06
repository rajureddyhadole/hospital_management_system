from django.shortcuts import render
from .models import Doctor
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def doctors_list(request):
  doctors = Doctor.objects.all()

  return render(request, 'doctor_list.html', {'doctors': doctors})