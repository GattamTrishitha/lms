from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.http import request

def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def libraryhomepage(request):
    return render(request, 'libraryhomepage.html')

def userhomepage(request):
    return render(request, 'userhomepage.html')

def login(request):
    return render(request, 'login.html')
def login1(request):
    if request.method == 'POST':
        username= request.POST['username']
        pass1=request.POST['password']
        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)

            if len(username)==10:
                return redirect('userhomepage')
            elif len(username)==4:
                return redirect('libraryhomepage')
            else:
                return redirect('projecthomepage')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'login.html')
    else:
        return(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return render(request, 'projecthomepage.html')
def signup(request):
    return render(request, 'signup.html')

def signup1(request):  # Fixing the parameter name to 'request'
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']  # Typo here as well, 'passsword' should be 'password'
        pass2 = request.POST['password1']

        if pass1 == pass2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully')
                return render(request, 'projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'signup.html')
