from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

 #Importing Required Forms and Models
from App_Login.models import UserProfile, Profile
from App_Login.forms import SignupForm,ProfileForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def sign_up(request):
    form = SignupForm()
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/sign_up.html', context={'form': form})

def login_user(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('logged in')
    return render(request, 'App_Login/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponse("Logged Out")