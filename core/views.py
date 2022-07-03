from urllib.robotparser import RequestRate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from requests import post
from .models import Profile

# Create your views here.


@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']

        if password == cpassword:
            if User.objects.filter(email=email).exists():
                # messages.info(request, {'message':'Email already exists','username':username,'email':email,'password':password})
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                # messages.info(request, {'message':'Username already exists','username':username,'email':email,'password':password})
                messages.info(request, 'Username already exists')

                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

                # Log user in and redirect to settings  page
                user_login = auth.authenticate(
                    username=username, password=password)
                auth.login(request, user_login)

                # Create profile model for user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, userid=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials are invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        pass

    return render(request, 'setting.html', {'user_profile': user_profile})

    # def profile(request):
#     return render(request,'profile.html
