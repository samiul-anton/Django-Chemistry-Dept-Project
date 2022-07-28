from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import labFacility as all_labfacilites

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
        return HttpResponseRedirect(reverse('lab_facilites'))
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
       return HttpResponseRedirect(reverse('lab_facilites'))
    else:
       return HttpResponseRedirect(reverse('index'))
