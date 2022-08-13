from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  #lab resource url
  path('all-lab-facility/', views.labFacility, name='admin_lab_facilites'),
  path('add/all-lab-facility/', views.addLabFacility, name='add_lab_facilites'),
  path('all-lab-facility/<int:id>/delete', views.deleteLabFacility, name='delete_lab_facilites'),
  path('all-lab-facility/edit/<int:id>', views.editLabFacility, name='edit_lab_facilites'),

  path('all-lab-facility/get/<int:id>', views.getLabResource, name='get_lab_facilites'),

   path('all-lab-facility/get/<int:id>', views.getLabResource, name='get_lab_facilites'),

  #computing url
  path('all-computing/', views.computing, name='admin_computing'),
  path('add-computing/', views.addComputing, name='add_computing'),
  path('all-computing/<int:id>/delete', views.deleteComputing, name='delete_computing'),
  path('all-computing/edit/<int:id>', views.editComputing, name='edit_computing'),
  path('all-computing/get/<int:id>', views.getComputing, name='get_computing'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
