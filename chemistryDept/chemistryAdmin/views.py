from django.shortcuts import render,redirect
from .models import research

def home(request):
    return render(request, 'chemistryAdmin/index.html')

def login(request):
    return render(request, 'chemistryAdmin/login.html')

def bschemistry(request):
    return render(request, 'chemistryAdmin/bschemistry.html')

def bschemical(request):
    return render(request, 'chemistryAdmin/bschemical.html')

def mschemistry(request):
    return render(request, 'chemistryAdmin/mschemistry.html')

def msbiomedical(request):
    return render(request, 'chemistryAdmin/msbiomedical.html')

def certificateprograms(request):
    return render(request, 'chemistryAdmin/certificateprograms.html')

def faculty(request):
    return render(request, 'chemistryAdmin/faculty.html')

def staff(request):
    return render(request, 'chemistryAdmin/staff.html')

def student(request):
    return render(request, 'chemistryAdmin/student.html')

def researchareachemistry(request):
    context = {
        'research': research.objects.all()
    }
    return render(request, 'chemistryAdmin/research-area-chemistry.html', {'data':context})

def researchdirectionsustainability(request):
    return render(request, 'chemistryAdmin/research-direction-sustainability.html')

def seminars(request):
    return render(request, 'chemistryAdmin/seminars.html')

def labfacility(request):
    return render(request, 'chemistryAdmin/labfacility.html')

def errorpage(request):
    return render(request, 'chemistryAdmin/404.html')

def contactpage(request):
    return render(request, 'chemistryAdmin/contact.html')

def AdminPanel(request):
    return render(request, 'AdminPanel/index.html')


