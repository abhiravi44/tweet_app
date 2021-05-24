from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
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
    posts=Post.objects.exclude(user=request.user)
    following=Following.objects.get(user=request.user)
    follo=following.following.all()
    print(follo)
    return render(request,'dashboard.html',{'form':form,'posts':posts,'follo':follo})

def all_users(request):
    users=User.objects.all()
    return render(request,'allusers.html',{'users':users})

def follow(request,id):
    try:
        user=User.objects.filter(id=id)
    except:
        messages.error(request,'User not found !!!')
        return redirect('dashboard')
    follow,created=Following.objects.get_or_create(user=request.user)
    if follow:
        follow.following.add(*user)
        follow.save()
    elif created:
        created.following.set(user)
        created.save()
    # print(follow)

    messages.success(request,f'You started following {user}')
    return redirect('dashboard')

def profile(request,id):
    user=get_object_or_404(User,pk=id)
    post=Post.objects.filter(user=user)
    return render(request,'profile.html',{'posts':post,'username':user})
