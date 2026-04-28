from django.urls import path
from .views import dashboard_home, dashboard_medha_ai

urlpatterns = [
  path('', dashboard_home),
  path('ai/', dashboard_medha_ai)
]