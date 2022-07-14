from django.shortcuts import render
from AdminPanel.models import faculty

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
