from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import faculty as all_faculty
from .models import staff as all_staff
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
       new_faculty.about = request.POST.get('faculty_about')
       new_faculty.url = request.POST.get('faculty_url')
       new_faculty.experience = request.POST.get('faculty_experience')
       new_faculty.faculty_image = request.FILES["faculty_image"]
       new_faculty.save()

       messages.success(request, 'New faculty added!')
       return HttpResponseRedirect(reverse('faculty'))

#delete faculty data
@login_required
def deleteFaculty(request,id):
    if request.method == "POST":
        all_faculty.objects.filter(id=id).delete()
        messages.success(request, 'Faculty Data Deleted!')
        return HttpResponseRedirect(reverse('faculty'))
    else:
        return HttpResponseRedirect(reverse('home'))
#view single faculty data
@login_required
def singleFaculty(request,id):
    faculty = all_faculty.objects.get(id=id)
    return render(request, 'peopleApp/singleFaculty.html',context={'faculty':faculty})


#admin staff view
@login_required
def staff(request):
    if request.method == "GET":
        data = all_staff.objects.all().order_by('name')
        return render(request, 'peopleApp/staff.html',context={'staff':data})
@login_required
def addStaff(request):
    if request.method == "POST":
       new_staff = all_staff()
       new_staff.name = request.POST.get('faculty_name')
       new_staff.email = request.POST.get('faculty_email')
       new_staff.designation = request.POST.get('faculty_designation')
       new_staff.staff_image = request.FILES["faculty_image"]
       new_staff.save()

       messages.success(request, 'New Staff added!')
       return HttpResponseRedirect(reverse('staff'))

#delete staff data
@login_required
def deleteStaff(request,id):
    if request.method == "POST":
        all_staff.objects.filter(id=id).delete()
        messages.success(request, 'Staff Data Deleted!')
        return HttpResponseRedirect(reverse('staff'))
    else:
        return HttpResponseRedirect(reverse('home'))
#admin student view
@login_required
def student(request):
    if request.method == "GET":
        return render(request, 'peopleApp/student.html',context={})
