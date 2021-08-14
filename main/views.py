from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from student.models import User

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def register_user(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created! You are now able to login.')
            return redirect('/')

    else:
        form = UserRegisterForm()
    return render(request,'main/register.html',{'form':form})



def logoutUser(request):
    logout(request)
    return render(request, 'main/logout.html',{ 'logout_message': 'Logged out Successfully' })

def login_success(request):
    if request.user.isStudent:
        # user is an admin
        return redirect("/student")
    else:
        return redirect("/prof")