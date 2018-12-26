from django.shortcuts import render
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def signin(request):
    form = UserForm(request.POST or None)
    ctx = {
        'form': form,
    }
    if form.is_valid():
        user = User(
            username = form.cleaned_data['username'],
            # ... here are passed the other fields
        )
        user.set_password(form.cleaned_data['password'])
        user.save()

        ctx['successfull'] = "User saved successfully"
    return render(request, 'users/signin.html', ctx)

def loginView(request):
    form = LoginForm(request.POST or None)
    ctx = {
        'form': form,
    }
    if form.is_valid():
        username =  request.POST['username']
        password =  request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            ctx['successfull'] = "user logged in"
        else:
            ctx['incorrect'] = "User or password doesn't match, try again"
    return render(request, 'users/login.html', ctx)
        
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
