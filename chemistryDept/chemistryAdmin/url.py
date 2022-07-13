from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminlogin/', views.login, name='adminlogin'),
    path('bschemistry/', views.bschemistry, name='bschemistry'),
    path('bschemical/', views.bschemical, name='bschemical'),
    path('mschemistry/', views.mschemistry, name='mschemistry'),
    path('msbiomedical/', views.msbiomedical, name='msbiomedical'),
    path('certificateprograms/', views.certificateprograms, name='certificateprograms'),
    path('faculty/', views.faculty, name='faculty'),
    path('staff/', views.staff, name='staff'),
    path('student/', views.student, name='student'),
    path('research-area-chemistry/', views.researchareachemistry, name='research-area-chemistry'),
    path('research-direction-sustainability/', views.researchdirectionsustainability, name='research-direction-sustainability'),
    path('seminars/', views.seminars, name='seminars'),
    path('labfacility/', views.labfacility, name='labfacility'),
    path('errorpage/', views.errorpage, name='errorpage'),
    path('contactpage/', views.contactpage, name='contactpage'),
    path('AdminPanel/', views.AdminPanel, name='AdminPanel'),
]
