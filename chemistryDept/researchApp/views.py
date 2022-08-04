from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import research_by_area,research_by_direction
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json

# Admin Research By Area View
@login_required
def researchByArea(request):
    if request.method == "GET":
        data = research_by_area.objects.all().order_by('research_title')
        return render(request, 'researchApp/researchByarea.html',context={'data':data})
#add new research by area
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

#delete research by area data
@login_required
def DeleteResearchByArea(request,id):
    if request.method == "POST":
        research_by_area.objects.filter(id=id).delete()
        messages.success(request, 'Research Data Deleted!')
        return HttpResponseRedirect(reverse('research_by_area'))
    else:
        return HttpResponseRedirect(reverse('index'))

@login_required
def singleResearchByArea(request,id):
    data = research_by_area.objects.get(id=id);
    return render(request, 'researchApp/SingleResearchByarea.html',context={'data':data})

@login_required
def researchAreaGetdata(request,id):
    researchData = research_by_area.objects.get(id=id)
    data = json.dumps(researchData.research_area_info())
    return JsonResponse({'data': data})

@login_required
def editResearchByArea(request,id):
    if request.method == "POST":
         research_area = research_by_area.objects.get(id=id)
         research_area.research_title = request.POST.get('research_title')
         research_area.research_fields = request.POST.get('research_fields')
         research_area.research_description = request.POST.get('research_description')
         research_area.project_include = request.POST.get('project_include')
         research_area.publication_video = request.POST.get('publication_video')
         research_area.publication_details = request.POST.get('publication_details')
         if bool(request.FILES.get('research_cover', False)) == True:
             research_area.research_cover = request.FILES["research_cover"]
         research_area.save()
         messages.success(request, 'Research data Updated!')
         return HttpResponseRedirect(reverse('research_by_area'))
    else:
        return HttpResponseRedirect(reverse('index'))

@login_required
def researchByDirection(request):
    if request.method == "GET":
        data = research_by_direction.objects.all().order_by('project_name')
        return render(request, 'researchApp/researchBydirection.html',context={'data':data})

@login_required
def addResearchByDirection(request):
    if request.method == "POST":
        new_research_by_direction = research_by_direction()
        new_research_by_direction.project_name = request.POST.get('project_name')
        new_research_by_direction.research_fields = request.POST.get('research_fields')
        new_research_by_direction.project_description = request.POST.get('project_description')
        new_research_by_direction.project_date = request.POST.get('project_date')
        new_research_by_direction.project_link = request.POST.get('project_link')
        new_research_by_direction.project_category = request.POST.get('project_category')
        new_research_by_direction.research_cover_1 = request.FILES["research_cover_1"]
        if request.FILES["research_cover_2"]:
            new_research_by_direction.research_cover_2 = request.FILES["research_cover_2"]
        if request.FILES["research_cover_3"]:
            new_research_by_direction.research_cover_3 = request.FILES["research_cover_3"]
        new_research_by_direction.save()

        messages.success(request, 'New Data added!')
        return HttpResponseRedirect(reverse('research_by_direction'))
@login_required
def DeleteResearchByDirection(request,id):
    if request.method == "POST":
        research_by_direction.objects.filter(id=id).delete()
        messages.success(request, 'Research Data Deleted!')
        return HttpResponseRedirect(reverse('research_by_direction'))
    else:
        return HttpResponseRedirect(reverse('index'))
@login_required
def singleResearchByDirection(request,id):
    data = research_by_direction.objects.get(id=id);
    return render(request, 'researchApp/SingleResearchBydirection.html',context={'data':data})

@login_required
def researchGetDirectionData(request,id):
    researchData = research_by_direction.objects.get(id=id)
    get_data = researchData.research_direction_info()
    #data = json.dumps(get_data)
    return JsonResponse({'data': get_data})

@login_required
def editResearchByDirection(request,id):
    pass
