from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Userinfo

from django.contrib.auth.models import User

#login page viewer
def login_page(request):
    if request.method == 'GET':
        return render(request,'AdminPanel/login.html')

#User login authenticator
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))

            else:
                return HttpResponse("Account Not Active")
        else:
            return HttpResponse("Wrong Login Credentials")
    else:
        return HttpResponseRedirect(reverse('login_page'))

#user logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

#Admin dashboard handler
def dashboard(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        try:
            user_info = Userinfo.objects.get(user__pk= user.id)
        except Userinfo.DoesNotExist:
            user_info = None

        return render(request,"AdminPanel/index.html",context={'user':user, 'user_info':user_info})
    else:
        return HttpResponseRedirect(reverse('login_page'))
