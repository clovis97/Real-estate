from django.shortcuts import render, redirect
from .forms  import CreateUserForm
from .models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def listings(request):
    return render(request, 'listings.html')
def search(request):
    return render(request, 'search.html')
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'registration/register.html', {'form': form})



def dashboard(request):
    return render(request, 'dashboard.html')
