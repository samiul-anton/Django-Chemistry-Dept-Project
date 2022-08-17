from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  #seminer url
  path('all-seminer/', views.allSeminers, name='seminers'),
  path('add-seminer/', views.addSeminer, name='add_seminer'),
  # path('add-faculty/', views.addFaculty, name='add_faculty'),
  # path('edit-faculty/<int:id>', views.editFaculty, name='edit_faculty'),
  # path('facutly/<int:id>', views.singleFaculty, name='single_faculty'),
  # path('faculty/getData/<int:id>', views.facultyGetdata, name='get_data'),
  # path('faculty/<int:id>/delete', views.deleteFaculty, name='delete_faculty'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
