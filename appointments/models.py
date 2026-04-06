from django.db import models

# Create your models here.
class Appointment(models.Model):
  patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
  doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
  appointment_date = models.DateTimeField()
  appointment_status = models.CharField(max_length=200)

  def __str__(self):
    return f"{self.patient} - {self.doctor}"