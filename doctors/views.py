from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor
from django.contrib.auth.decorators import login_required
from .forms import DoctorForm

# Create your views here.
@login_required
def doctors_list(request):
  doctors = Doctor.objects.all()

  return render(request, 'doctor_list.html', {'doctors': doctors})


@login_required
def doctor_edit(request, pk):
  doctor = get_object_or_404(Doctor, pk=pk)

  if request.method == 'POST':
    form = DoctorForm(request.POST)

    if form.is_valid():
      doctor.name = form.cleaned_data['name']
      doctor.specialization = form.cleaned_data['specialization']
      doctor.save()
      return redirect('/doctors')
  else:
    form = DoctorForm(initial={
      'name': doctor.name,
      'specialization': doctor.specialization
    })

  return render(request, 'doctor_edit.html', {'form': form})


@login_required
def doctor_create(request):
  if request.method == 'POST':
    form = DoctorForm(request.POST)

    if form.is_valid():
      
      Doctor.objects.create(
        name = form.cleaned_data['name'],
        specialization = form.cleaned_data['specialization']
      )
      return redirect('/doctors')
  else:
    form = DoctorForm()

  return render(request, 'doctor_create.html', {'form': form})


@login_required
def doctor_delete(request, pk):
  doctor = get_object_or_404(Doctor, pk=pk)

  doctor.delete()

  return redirect('/doctors')


from rest_framework.generics import ListCreateAPIView
from .serializers import DoctorSerializer

class DoctorListCreateAPI(ListCreateAPIView):
  queryset = Doctor.objects.all()
  serializer_class = DoctorSerializer