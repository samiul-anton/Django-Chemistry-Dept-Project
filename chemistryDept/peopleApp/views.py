from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import faculty as all_faculty


#admin faculty view
@login_required
def faculty(request):
    if request.method == "GET":
        data = all_faculty.objects.all().order_by('name')
        return render(request, 'peopleApp/faculty.html',context={'faculty':data})
#admin faculty view
@login_required
def staff(request):
    if request.method == "GET":
        return render(request, 'peopleApp/staff.html',context={})
#admin faculty view
@login_required
def student(request):
    if request.method == "GET":
        return render(request, 'peopleApp/student.html',context={})
