from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                return HttpResponse("Invalid username or password.")
        else:
            return HttpResponse("Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form})


def new_user(request):
    return HttpResponse("Registration page in WIP")

def reset_pass(request):
    return HttpResponse("Pass reset page in WIP")