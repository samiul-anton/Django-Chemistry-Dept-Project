from django.shortcuts import render
from researchApp.models import research_by_area, research_by_direction
from peopleApp.models import faculty,staff,student
from resourceApp.models import labFacility
from resourceApp.models import computing as all_computing
#Home page view

def index(request):
    data = {}
    return render(request,'HomeApp/index.html',context=data)


#About page view

def contact(request):
    data = {}
    return render(request,'HomeApp/contact.html',context=data)

#Faculty page view

def facultys(request):
    data = faculty.objects.order_by('name')
    return render(request,'HomeApp/faculty.html',context={'faculty':data})

#Staff page view

def staffs(request):
    data = staff.objects.order_by('name')
    return render(request,'HomeApp/staff.html',context={'staff':data})

#Student page view

def students(request):
    undergrad_student = student.objects.filter(student_type="Undergrad").order_by('name')
    grad_student = student.objects.filter(student_type="Graduate").order_by('name')
    return render(request,'HomeApp/student.html',context={'undergrad_student':undergrad_student,'grad_student':grad_student})

#bschemistry page view

def bschemistry(request):
    return render(request, 'HomeApp/bschemistry.html')

#bschemical page view

def bschemical(request):
    return render(request, 'HomeApp/bschemical.html')

#mschemistry page view

def mschemistry(request):
    return render(request, 'HomeApp/mschemistry.html')

#msbiomedical page view

def msbiomedical(request):
    return render(request, 'HomeApp/msbiomedical.html')

#certificateprograms page view

def certificateprograms(request):
    return render(request, 'HomeApp/certificateprograms.html')

#Research by area view page

def researchChemistry(request):
    data = research_by_area.objects.filter(research_fields="Chemistry")
    return render(request, 'HomeApp/research-area.html' , context={'title':"Chemistry",'research': data})
def researchChemical(request):
    data = research_by_area.objects.filter(research_fields="Chemical Engineering")
    return render(request, 'HomeApp/research-area.html' , context={'title':"Chemical Engineering",'research': data})
def researchBiomedical(request):
    data = research_by_area.objects.filter(research_fields="Biomedical Engineering")
    return render(request, 'HomeApp/research-area.html' , context={'title':"Biomedical Engineering",'research': data})


#Research by direction view page
def researchSustainabilityEnergy(request):
    data = research_by_direction.objects.filter(research_fields="Sustainability Energy")
    return render(request, 'HomeApp/research-direction.html',context={'title':"Sustainability Energy",'research': data})
def researchMedical(request):
    data = research_by_direction.objects.filter(research_fields="Medical")
    return render(request, 'HomeApp/research-direction.html',context={'title':"Medical",'research': data})

#Events view Page
def courseAnnouncements(request):
    return render(request, 'HomeApp/courseAnnouncements.html')
def seminars(request):
    return render(request, 'HomeApp/seminars.html')

#Resources view page
def labFacilites(request):
    data = labFacility.objects.all()
    return render(request, 'HomeApp/labFacilites.html',context={'data':data})
def computing(request):
    image_data = all_computing.objects.filter(computing_type="Image")
    video_data = all_computing.objects.filter(computing_type="Video")
    return render(request, 'HomeApp/computing.html',context={"image_data":image_data,"video_data":video_data})
def studentServices(request):
    return render(request, 'HomeApp/studentServices.html')

#News view page
def news(request):
    return render(request, 'HomeApp/news.html')

#Dummy for test
def dummy(request):
    return render(request, 'HomeApp/dummytest.html')
