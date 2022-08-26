from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import new
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json

# Create your views here.

#admin news view
@login_required
def allNews(request):
    data = new.objects.all().order_by('news_title')
    return render(request, 'newsApp/news.html',context={'data':data})
