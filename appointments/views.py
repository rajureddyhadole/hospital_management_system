from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment

# Create your views here.
@login_required
def appointments_list(request):
  appointments = Appointment.objects.all()

  return render(request, 'appointments_list.html', {'appointments': appointments})


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