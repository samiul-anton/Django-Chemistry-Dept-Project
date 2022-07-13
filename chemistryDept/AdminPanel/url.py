from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminPanel, name='AdminPanel'),
    path('Adminprofile/', views.Adminprofile, name='Adminprofile'),
    path('people/', views.people, name='people'),
    path('blank/', views.blank, name='blank'),
]