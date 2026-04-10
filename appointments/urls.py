from django.urls import path
from .views import appointments_list, appointment_edit, appointment_delete, appointment_create

urlpatterns = [
  path('', appointments_list),
  path('<int:pk>/edit/', appointment_edit),
  path('<int:pk>/delete/', appointment_delete),
  path('create/', appointment_create)
]