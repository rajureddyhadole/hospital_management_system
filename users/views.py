from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    user = User.objects.create_user(
      username=username,
      password=password
    )
    login(request, user)
    return redirect('/dashboard')
  else:
    return render(request, 'user_signup.html')
  

def user_login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user:
      login(request, user)
      return redirect('/dashboard')
    else:
      print("user does not exists")
  
  return render(request, 'user_login.html')


def user_logout(request):
  logout(request)
  return redirect('/login')