from django.shortcuts import render, redirect
from .models import Team
from .forms import RegistrationForm


def index(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'index.html', context)

def user_registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # messages.success(request, 'You have singed up successfully.')
            # login(request, user)
            return redirect('/')
    return render(request, 'registration_form.html', {'form': form})

# Create your views here.
