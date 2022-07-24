from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import research_by_area
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse

# Admin Reseach By Area View
@login_required
def researchByArea(request):
    if request.method == "GET":
        data = research_by_area.objects.all().order_by('research_title')
        return render(request, 'researchApp/researchByarea.html',context={'data':data})

def addResearchByArea(request):
    if request.method == "POST":
       new_research_by_area = research_by_area()
       new_research_by_area.research_title = request.POST.get('research_title')
       new_research_by_area.research_fields = request.POST.get('research_fields')
       new_research_by_area.research_description = request.POST.get('research_description')
       new_research_by_area.project_include = request.POST.get('project_include')
       new_research_by_area.publication_video = request.POST.get('publication_video')
       new_research_by_area.publication_details = request.POST.get('publication_details')
       new_research_by_area.research_cover = request.FILES["research_cover"]
       new_research_by_area.save()

       messages.success(request, 'New Data added!')
       return HttpResponseRedirect(reverse('research_by_area'))

#delete research data
@login_required
def DeleteResearchByArea(request,id):
    if request.method == "POST":
        research_by_area.objects.filter(id=id).delete()
        messages.success(request, 'Research Data Deleted!')
        return HttpResponseRedirect(reverse('research_by_area'))
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required
def researchByDirection(request):
    pass
