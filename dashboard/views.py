from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from google import genai
from django.conf import settings
from doctors.models import Doctor
from patients.models import Patient

# Create your views here.
@login_required
def dashboard_home(request):
  return render(request, 'dashboard_home.html')


@login_required
def dashboard_medha_ai(request):
  if request.method == 'POST':
    user_query = request.POST.get('query')

    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    doctors = list(doctors.values())
    patients = list(patients.values())

    final_query = f'''You are the AI chatbot inside a website called medhaHMS
    Your responsibility is to answer questions about medhaHMS data.
    Anything apart from this, you are not allowed to answer.
    Below is the doctor data you need to know.
    {doctors} and below are patients {patients}
    
    Answer below:
    {user_query}'''

    client  = genai.Client(api_key=settings.GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= final_query,
    )


    answer = response.text

    return render(request, 'dashboard_medha_ai.html', {'answer': answer})
  return render(request, 'dashboard_medha_ai.html')

