from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor

# Create your views here.
@login_required
def appointments_list(request):
  appointments = Appointment.objects.all()

  return render(request, 'appointments_list.html', {'appointments': appointments})


@login_required
def appointment_edit(request, pk):
  appointment = get_object_or_404(Appointment, pk=pk)

  if request.method == 'POST':
    appointment.patient.name = request.POST.get('patient')
    appointment.patient.save()

    appointment.doctor.name = request.POST.get('doctor')
    appointment.doctor.save()
    
    appointment.appointment_time = request.POST.get('time')
    appointment.appointment_status = request.POST.get('status')
    appointment.save()
    return redirect('/appointments')

  return render(request, 'appointment_edit.html', {'appointment': appointment})


@login_required
def appointment_delete(request, pk):
  appointment = get_object_or_404(Appointment, pk=pk)

  appointment.delete()

  return redirect('/appointments')


@login_required
def appointment_create(request):

  if request.method == 'POST':
    patient = Patient.objects.get(id=request.POST.get('patient'))
    doctor = Doctor.objects.get(id=request.POST.get('doctor'))

    from datetime import datetime
    time = datetime.fromisoformat(request.POST.get('time'))

    status = request.POST.get('status')

    Appointment.objects.create(
      patient = patient,
      doctor = doctor,
      appointment_time = time,
      appointment_status = status
    )
    return redirect('/appointments')
  
  #GET request
  patients = Patient.objects.all()
  doctors = Doctor.objects.all()

  return render(request, 'appointment_create.html', {'patients': patients, 'doctors': doctors})