from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
 # Basic urls
  path('', views.index, name='index'),
  path('contact/', views.contact, name='contact'),
  # People urls
  path('faculty/', views.facultys, name='view_faculty'),
  path('staff/', views.staffs, name='view_staff'),
  path('student/', views.students, name='view_student'),
  # Academic urls
  path('bschemistry/', views.bschemistry, name='bschemistry'),
  path('bschemical/', views.bschemical, name='bschemical'),
  path('mschemistry/', views.mschemistry, name='mschemistry'),
  path('msbiomedical/', views.msbiomedical, name='msbiomedical'),
  path('certificateprograms/', views.certificateprograms, name='certificateprograms'),
  # Research by area urls
  path('research-chemistry/', views.researchChemistry, name='research_chemistry'),
  path('research-chemical/', views.researchChemical, name='research_chemical'),
  path('research-biomedical/', views.researchBiomedical, name='research_biomedical'),
  # Research by direction urls
  path('research-sustainability-Energy/', views.researchSustainabilityEnergy, name='research_s_energy'),
  path('research-medical/', views.researchMedical, name='research_medical'),
  # Events urls
  path('course-announcements/', views.courseAnnouncements, name='course_announcements'),
  path('seminars/', views.seminars, name='seminars'),
  # Resources urls
  path('lab-facilites/', views.labFacilites, name='lab_facilites'),
  path('computing/', views.computing, name='computing'),
  path('student-services/', views.studentServices, name='student_services'),
  # News url
  path('news/', views.news, name='news'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
