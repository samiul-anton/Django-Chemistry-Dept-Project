from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import faculty

def AdminPanel(request):
    return render(request, 'AdminPanel/index.html')

def Adminprofile(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('Adminprofile')
    else:
        form = UserRegisterForm()
    return render(request, 'AdminPanel/profile.html', {'form': form})

def people(request):
    if request.method == 'POST':
        prof = faculty()
        prof.name = request.POST.get('name')
        prof.email = request.POST.get('email')
        prof.designation = request.POST.get('designation')
        prof.experience = request.POST.get('experience')
        prof.about = request.POST.get('about')
        if len(request.FILES) != 0:
            prof.faculty_image = request.FILES['faculty_image']

        prof.save()
        messages.success(request, f'data saved!!!')

    professors = faculty.objects.all()
    context = {'professors' : professors}
    return render(request, 'AdminPanel/people.html', context)

def blank(request):
    return render(request, 'AdminPanel/blank.html')
