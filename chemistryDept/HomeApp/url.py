from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  path('', views.index, name='index'),
  path('contact/', views.contact, name='about'),
  path('faculty/', views.facultys, name='faculty'),
  path('staff/', views.staffs, name='staff'),
  path('bschemistry/', views.bschemistry, name='bschemistry'),
  path('bschemical/', views.bschemical, name='bschemical'),
  path('mschemistry/', views.mschemistry, name='mschemistry'),
  path('msbiomedical/', views.msbiomedical, name='msbiomedical'),
  path('certificateprograms/', views.certificateprograms, name='certificateprograms'),
  path('research_chemistry/', views.researchChemistry, name='research_chemistry'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
