from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  path('all-lab-facility/', views.labFacility, name='admin_lab_facilites'),
  path('add/all-lab-facility/', views.addLabFacility, name='add_lab_facilites'),
  path('all-lab-facility/<int:id>/delete', views.deleteLabFacility, name='delete_lab_facilites'),
  path('all-computing/', views.computing, name='admin_computing'),
  path('add-computing/', views.addComputing, name='add_computing'),
  path('all-computing/<int:id>/delete', views.deleteComputing, name='delete_computing'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
