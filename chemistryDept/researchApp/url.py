from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  path('by-area/', views.researchByArea, name='research_by_area'),
  path('by-area/add', views.addResearchByArea, name='add_research_by_area'),
  path('by-direction/', views.researchByDirection, name='research_by_direction'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
