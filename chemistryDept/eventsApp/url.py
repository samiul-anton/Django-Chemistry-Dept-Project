from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  #seminer url
  path('all-seminer/', views.allSeminers, name='seminers'),
  path('add-seminer/', views.addSeminer, name='add_seminer'),
  path('seminer/<int:id>/delete', views.deleteSeminer, name='delete_seminer'),
  path('edit-seminer/<int:id>', views.editSeminer, name='edit_seminer'),
  path('seminer/getData/<int:id>', views.getSeminerData, name='get_seminer_data'),
  # path('add-faculty/', views.addFaculty, name='add_faculty'),

  # path('facutly/<int:id>', views.singleFaculty, name='single_faculty'),
  # path('faculty/getData/<int:id>', views.facultyGetdata, name='get_data'),
  # path('faculty/<int:id>/delete', views.deleteFaculty, name='delete_faculty'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
