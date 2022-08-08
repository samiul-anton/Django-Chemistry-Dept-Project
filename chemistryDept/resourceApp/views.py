from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .models import labFacility as all_labfacilites
from .models import computing as all_computing
import json

# View All lab facility image.
@login_required
def labFacility(request):
    data = all_labfacilites.objects.all()
    return render(request,'resourceApp/lab_resource.html',context={"data":data})
# Delete All lab facility
@login_required
def deleteLabFacility(request,id):
    if request.method == "POST":
        all_labfacilites.objects.filter(id=id).delete()
        messages.success(request, 'Data Deleted!')
        return HttpResponseRedirect(reverse('admin_lab_facilites'))
    else:
        return HttpResponseRedirect(reverse('home'))
@login_required
def addLabFacility(request):
    if request.method == "POST":
       new_lab_resource = all_labfacilites()
       new_lab_resource.image_heading = request.POST.get('image_heading')
       new_lab_resource.image_caption = request.POST.get('image_caption')
       new_lab_resource.lab_image = request.FILES["lab_image"]
       new_lab_resource.save()

       messages.success(request, 'New data added!')
       return HttpResponseRedirect(reverse('admin_lab_facilites'))
    else:
       return HttpResponseRedirect(reverse('index'))

@login_required
def computing(request):
    data = all_computing.objects.all()
    return render(request,'resourceApp/computing.html',context={"data":data})
@login_required
def addComputing(request):
    if request.method == "POST":
       new_computing = all_computing()
       new_computing.computing_heading = request.POST.get('computing_heading')
       new_computing.computing_type = request.POST.get('computing_type')
       if request.POST.get('computing_type') == "Image":
           new_computing.computing_image = request.FILES["computing_image"]
       else:
           new_computing.computing_url = request.POST.get('computing_url')
       new_computing.save()
       messages.success(request, 'New data added!')
       return HttpResponseRedirect(reverse('admin_computing'))
    else:
       return HttpResponseRedirect(reverse('index'))
@login_required
def deleteComputing(request,id):
    if request.method == "POST":
        all_computing.objects.filter(id=id).delete()
        messages.success(request, 'Data Deleted!')
        return HttpResponseRedirect(reverse('admin_computing'))
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required
def editLabFacility(request,id):
    if request.method == "POST":
       labFacility = all_labfacilites.objects.get(id=id)
       labFacility.image_heading = request.POST.get('image_heading_edit')
       labFacility.image_caption = request.POST.get('image_caption_edit')
       if bool(request.FILES.get('image_edit', False)) == True:
           labFacility.lab_image = request.FILES["image_edit"]
       labFacility.save()

       messages.success(request, 'Data Updated!')
       return HttpResponseRedirect(reverse('admin_lab_facilites'))
    else:
       return HttpResponseRedirect(reverse('index'))

@login_required
def getLabResource(request ,id ):
    labFacility = all_labfacilites.objects.get(id=id)
    get_data = json.dumps(labFacility.all_labfacilites_data())
    return JsonResponse({'data': get_data})
