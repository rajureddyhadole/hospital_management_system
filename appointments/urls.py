from django.urls import path
from .views import appointments_list, appointment_edit

urlpatterns = [
  path('', appointments_list),
  path('<int:pk>/edit/', appointment_edit)
]