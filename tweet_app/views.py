from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *
from .models import *


# Create your views here.
def signin(request):
    if request.method =='POST':
        form = LoginForm(request.POST or None)
        if request.POST and form.is_valid():
            user = form.login(request)
            # print(user)
            if user:
                login(request, user)
                return redirect('dashboard')

        else:
            messages.error(request,'Invalid credentials !!!')
            return render(request,'registration/login.html',{'form':form })
    else:
        form=LoginForm()
    return render(request,'registration/login.html',{'form':form })

def dashboard(request):
    if request.method =='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('dashboard')
        else:
            messages.error(request,form.errors)
            return redirect('dashboard')

    form=PostForm()
    posts=Post.objects.all()
    return render(request,'dashboard.html',{'form':form,'posts':posts})
