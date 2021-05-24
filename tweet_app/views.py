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
                if user.is_manager:
                    return redirect('manager:dashboard')
                else:
                    return redirect('staff:dashboard')
            # return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials !!!')
            return render(request,'registration/login.html',{'form':form })
    else:
        form=LoginForm()
    return render(request,'registration/login.html',{'form':form })

# Create your views here.
