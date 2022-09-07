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
  #course announcement url
  path('courses/', views.allCourses, name='courses'),
  path('add-course/', views.addCourse, name='add_course'),
  path('course/<int:id>/delete', views.deleteCourse, name='delete_course'),
  path('courses/getData/<int:id>', views.getCourseData, name='get_data'),
  path('edit-course/<int:id>', views.editCourse, name='edit_course'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
