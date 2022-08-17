from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json
from .models import seminer

# All Seminars
@login_required
def allSeminers(request):
    data = seminer.objects.all().order_by('seminer_datetime')
    return render(request, 'eventsApp/seminers.html',context={'data':data})

# Add seminer
def addSeminer(request):
    if request.method == "POST":
       new_seminer = seminer()
       new_seminer.seminer_title = request.POST.get('seminer_title')
       new_seminer.seminer_description = request.POST.get('seminer_description')
       new_seminer.seminer_details = request.POST.get('seminer_details')
       new_seminer.seminer_speakers = request.POST.get('seminer_speakers')
       new_seminer.seminer_location = request.POST.get('seminer_location')
       new_seminer.seminer_datetime = request.POST.get('seminer_datetime')
       new_seminer.seminar_cover = request.FILES["seminar_cover"]
       new_seminer.featured = request.POST.get('featured')
       new_seminer.save()

       messages.success(request, 'New Seminer added!')
       return HttpResponseRedirect(reverse('seminers'))
