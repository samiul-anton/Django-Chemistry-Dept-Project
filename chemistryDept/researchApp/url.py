from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  #Research Overview
  path('overview/', views.researchOverview, name='research_overview'),
  path('overview/add', views.addResearchOverview, name='add_research_overview'),
  path('overview/<int:id>/delete', views.DeleteResearchOverview, name='delete_research_overview'),
  path('overview/edit-research-area/<int:id>', views.editResearchByArea, name='edit_research_area'),
  path('overview/getData/<int:id>', views.researchOverviewGetdata, name='research_overview_get_data'),
  #Research By area URL
  path('by-area/', views.researchByArea, name='research_by_area'),
  path('by-area/add', views.addResearchByArea, name='add_research_by_area'),
  path('by-area/<int:id>/delete', views.DeleteResearchByArea, name='delete_research_by_area'),
  path('by-area/<int:id>/view', views.singleResearchByArea, name='single_research_by_area'),
  path('by-area/edit-research-area/<int:id>', views.editResearchByArea, name='edit_research_area'),
  path('by-area/getData/<int:id>', views.researchAreaGetdata, name='research_get_data'),
  #Research By direction URL
  path('by-direction/', views.researchByDirection, name='research_by_direction'),
  path('by-direction/add', views.addResearchByDirection, name='add_research_by_direction'),
  path('by-direction/<int:id>/delete', views.DeleteResearchByDirection, name='delete_research_by_direction'),
  path('by-direction/<int:id>/view', views.singleResearchByDirection, name='single_research_by_direction'),
  path('by-direction/edit-research-area/<int:id>', views.editResearchByDirection, name='edit_research_direction'),
  path('by-direction/getData/<int:id>', views.researchGetDirectionData, name='research_get_direction'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
