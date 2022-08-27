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
#admin news add
@login_required
def addNews(request):
    if request.method == "POST":
       new_news = new()
       new_news.news_title = request.POST.get('news_title')
       new_news.news_description = request.POST.get('news_description')
       new_news.news_category = request.POST.get('news_category')
       new_news.news_url = request.POST.get('news_url')
       new_news.news_cover = request.FILES["news_cover"]
       new_news.save()

       messages.success(request, 'New news added!')
       return HttpResponseRedirect(reverse('all_news'))
    else:
       return HttpResponseRedirect(reverse('index'))
