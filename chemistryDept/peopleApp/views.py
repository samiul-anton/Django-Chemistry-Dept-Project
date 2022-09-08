from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import faculty as all_faculty
from .models import staff as all_staff
from .models import student as all_student
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json


#admin faculty view
@login_required
def faculty(request):
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
    else:
       return HttpResponseRedirect(reverse('index'))

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

#Getting a single faculty data
@login_required
def facultyGetdata(request,id):
    facultyData = all_faculty.objects.get(id=id)
    data = json.dumps(facultyData.faculty_info())
    return JsonResponse({'data': data})

#edit a single faculty
@login_required
def editFaculty(request,id):
    if request.method == "POST":
       faculty = all_faculty.objects.get(id=id)
       faculty.name = request.POST.get('faculty_name')
       faculty.email = request.POST.get('faculty_email')
       faculty.designation = request.POST.get('faculty_designation')
       faculty.about = request.POST.get('faculty_about')
       faculty.url = request.POST.get('faculty_url')
       faculty.experience = request.POST.get('faculty_experience')
       #filepath = request.FILES["faculty_image"].name
       if bool(request.FILES.get('faculty_image', False)) == True:
         faculty.faculty_image = request.FILES["faculty_image"]
       faculty.save()
       messages.success(request, 'Faculty data changed!')
       return HttpResponseRedirect(reverse('faculty'))
    else:
       return HttpResponseRedirect(reverse('index'))

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
       new_staff.description = request.POST.get('description')
       new_staff.staff_image = request.FILES["faculty_image"]
       new_staff.save()

       messages.success(request, 'New Staff added!')
       return HttpResponseRedirect(reverse('staff'))
    else:
       return HttpResponseRedirect(reverse('index'))

#edit staff data
def editStaff(request,id):
    if request.method == "POST":
       new_staff = all_staff.objects.get(id=id)
       new_staff.name = request.POST.get('staff_name')
       new_staff.email = request.POST.get('staff_email')
       new_staff.designation = request.POST.get('staff_designation')
       new_staff.description = request.POST.get('staff_description')
       if bool(request.FILES.get('staff_image', False)) == True:
         new_staff.staff_image = request.FILES["staff_image"]
       new_staff.save()

       messages.success(request, 'Staff Data Updated!')
       return HttpResponseRedirect(reverse('staff'))
    else:
       return HttpResponseRedirect(reverse('home'))
def staffGetdata(request,id):
    staffData = all_staff.objects.get(id=id)
    data = json.dumps(staffData.staff_info())
    return JsonResponse({'data': data})



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
        data = all_student.objects.all().order_by('name')
        return render(request, 'peopleApp/student.html',context={'student':data})
#add student data
@login_required
def addStudents(request):
    if request.method == "POST":
       new_student = all_student()
       new_student.name = request.POST.get('student_name')
       new_student.email = request.POST.get('student_email')
       new_student.student_type = request.POST.get('student_type')
       new_student.student_image = request.FILES["student_image"]
       new_student.save()

       messages.success(request, 'New Student added!')
       return HttpResponseRedirect(reverse('student'))
    else:
       return HttpResponseRedirect(reverse('index'))

#getting student data for edit modal
@login_required
def studentGetdata(request,id):
    studentData = all_student.objects.get(id=id)
    data = json.dumps(studentData.student_info())
    return JsonResponse({'data': data})

#delete student data
@login_required
def deleteStudent(request,id):
    if request.method == "POST":
        all_student.objects.filter(id=id).delete()
        messages.success(request, 'Student Data Deleted!')
        return HttpResponseRedirect(reverse('student'))
    else:
        return HttpResponseRedirect(reverse('home'))

#Edit the student data
@login_required
def editStudent(request,id):
    if request.method == "POST":
       student = all_student.objects.get(id=id)
       student.name = request.POST.get('student_name')
       student.email = request.POST.get('student_email')
       student.student_type = request.POST.get('student_type')
       if bool(request.FILES.get('student_image', False)) == True:
         student.student_image = request.FILES["student_image"]
       student.save()

       messages.success(request, 'Student Data Updated!')
       return HttpResponseRedirect(reverse('student'))
    else:
       return HttpResponseRedirect(reverse('index'))
