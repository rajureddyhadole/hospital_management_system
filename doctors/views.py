from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def doctors_list(request):
  doctors = Doctor.objects.all()

  return render(request, 'doctor_list.html', {'doctors': doctors})


@login_required
def doctor_edit(request, pk):
  doctor = get_object_or_404(Doctor, pk=pk)

  if request.method == 'POST':
    doctor.name = request.POST.get('name')
    doctor.specialization = request.POST.get('specialization')
    doctor.save()
    return redirect('/doctors')

  return render(request, 'doctor_edit.html', {'doctor': doctor})


@login_required
def doctor_create(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    specialization = request.POST.get('specialization')

    Doctor.objects.create(
      name = name,
      specialization = specialization
    )
    return redirect('/doctors')
  return render(request, 'doctor_create.html')


@login_required
def doctor_delete(request, pk):
  doctor = get_object_or_404(Doctor, pk=pk)

  doctor.delete()

  return redirect('/doctors')