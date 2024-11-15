from django.shortcuts import render
from .models import Team


def index(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'index.html', context)

# Create your views here.
