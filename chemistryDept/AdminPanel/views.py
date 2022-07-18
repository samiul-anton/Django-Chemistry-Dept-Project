from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
        return render(request,"AdminPanel/index.html",context={'user':user})
    else:
        return HttpResponseRedirect(reverse('login_page'))







# from django.contrib import messages
# from .forms import UserRegisterForm
# from .models import faculty

# def AdminPanel(request):
#     return render(request, 'AdminPanel/index.html')
#
# def Adminprofile(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('Adminprofile')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'AdminPanel/profile.html', {'form': form})
#
# def people(request):
#     if request.method == 'POST':
#         prof = faculty()
#         prof.name = request.POST.get('name')
#         prof.email = request.POST.get('email')
#         prof.designation = request.POST.get('designation')
#         prof.experience = request.POST.get('experience')
#         prof.about = request.POST.get('about')
#         if len(request.FILES) != 0:
#             prof.faculty_image = request.FILES['faculty_image']
#
#         prof.save()
#         messages.success(request, f'data saved!!!')
#
#     professors = faculty.objects.all()
#     context = {'professors' : professors}
#     return render(request, 'AdminPanel/people.html', context)
#
# def blank(request):
#     return render(request, 'AdminPanel/blank.html')
