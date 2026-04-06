from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def patient_list(request):
  patients = Patient.objects.all()
  return render(request, 'list.html', {"patients": patients})
