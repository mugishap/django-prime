from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']

        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                # se in
        else:
            messages.info(request,'Passwords do not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')

    # def profile(request):
#     return render(request,'profile.html')

# def settings(request):
#     return render(request,'setting.html')

# def signin(request):
#     return render(request,'signin.html')

