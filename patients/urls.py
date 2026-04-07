from django.urls import path
from .views import patient_list, patient_edit, patient_create, patient_delete

urlpatterns = [
  path('', patient_list),
  path('<int:pk>/edit', patient_edit),
  path('create/', patient_create),
  path('<int:pk>/delete/', patient_delete)
]