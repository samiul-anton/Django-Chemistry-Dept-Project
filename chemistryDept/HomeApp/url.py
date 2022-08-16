from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
 # Basic urls
  path('', views.index, name='index'),
  # People urls
  path('people/faculty/', views.facultys, name='view_faculty'),
  path('people/staff/', views.staffs, name='view_staff'),
  path('people/student/', views.students, name='view_student'),
  # Academic urls
  path('academic/bschemistry/', views.bschemistry, name='bschemistry'),
  path('academic/bschemical/', views.bschemical, name='bschemical'),
  path('academic/mschemistry/', views.mschemistry, name='mschemistry'),
  path('academic/msbiomedical/', views.msbiomedical, name='msbiomedical'),
  path('academic/certificateprograms/', views.certificateprograms, name='certificateprograms'),
  path('academic/phdprogram/', views.phdprogram, name='phdprogram'),
  # Research by area urls
  path('research-by-area/chemistry/', views.researchChemistry, name='research_chemistry'),
  path('research-by-area/chemical/', views.researchChemical, name='research_chemical'),
  path('research-by-area/biomedical/', views.researchBiomedical, name='research_biomedical'),

  # Research by direction urls
  path('researchoverview/', views.researchoverview, name='researchoverview'),
  path('research-by-direction/sustainability-Energy/', views.researchSustainabilityEnergy, name='research_s_energy'),
  path('research-by-direction/medical', views.researchMedical, name='research_medical'),
  # Events urls
  path('teaching-events/course-announcements/', views.courseAnnouncements, name='course_announcements'),
  path('teaching-events/seminars/', views.seminars, name='seminars'),
  # Resources urls
  path('resource/lab-facilites/', views.labFacilites, name='lab_facilites'),
  path('resource/computing/', views.computing, name='computing'),
  path('resource/student-services/', views.studentServices, name='student_services'),
  # News url
  path('news/', views.news, name='news'),


  #About
  path('contact/', views.contact, name='contact'),
  path('chairletter/', views.chairletter, name='chairletter'),
  path('missionvision/', views.missionvision, name='missionvision'),


  #DummyTest
  path('dummy/', views.dummy, name='dummy'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
