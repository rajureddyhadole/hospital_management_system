from django import forms

class DoctorForm(forms.Form):
  name = forms.CharField(max_length=200)
  specialization = forms.CharField(max_length=200)