from django.shortcuts import render
from .models import User

def index(request):
    return render(request, 'index.html')

def start_game(request):
    return render(request, 'new_game.html')