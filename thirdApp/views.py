from django.shortcuts import render, redirect
from .models import Team, CustomUser
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm

@login_required(login_url='login')
def index(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'index.html', context)

def user_registration(request):  # sourcery skip: extract-method
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('/')
    return render(request, 'registration_form.html', {'form': form})

def login_user(request):
    if request.method != 'POST':
        return render (request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user= CustomUser.objects.get(username=username)
        # user.set_password(password)
    except CustomUser.DoesNotExist:
        messages.error(request, 'username does not exist!')
        return render (request, 'login.html')
    user = authenticate(request, username=username, password=password)

    if user is None:
        messages.error(request, 'Incorrect password')
        return render (request, 'login.html')

    elif user.is_active:
        login(request, user)
        messages.success(request, 'Logged in succesfully')
    else:
        messages.error(request, 'Please activate your account')
        return render (request, 'login.html')
    return redirect('/')
    
def logout_user(request):
    logout(request)
    return redirect('login')
# Create your views here.
