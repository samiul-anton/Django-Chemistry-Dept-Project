from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import faculty as all_faculty
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse


#admin faculty view
@login_required
def faculty(request):
    if request.method == "GET":
        data = all_faculty.objects.all().order_by('name')
        return render(request, 'peopleApp/faculty.html',context={'faculty':data})

@login_required
def addFaculty(request):
    if request.method == "POST":
       new_faculty = all_faculty()
       new_faculty.name = request.POST.get('faculty_name')
       new_faculty.email = request.POST.get('faculty_email')
       new_faculty.designation = request.POST.get('faculty_designation')
       new_faculty.about = request.POST.get('facutly_about')
       new_faculty.experience = request.POST.get('faculty_experience')
       new_faculty.faculty_image = request.FILES["faculty_image"]
       new_faculty.save()

       messages.success(request, 'New faculty added!')
       return HttpResponseRedirect(reverse('faculty'))

#admin staff view
@login_required
def staff(request):
    if request.method == "GET":
        return render(request, 'peopleApp/staff.html',context={})
#admin student view
@login_required
def student(request):
    if request.method == "GET":
        return render(request, 'peopleApp/student.html',context={})
