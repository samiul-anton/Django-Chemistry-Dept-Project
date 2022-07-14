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
