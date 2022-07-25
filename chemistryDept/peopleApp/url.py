from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  path('all-facultys/', views.faculty, name='faculty'),
  path('add-faculty/', views.addFaculty, name='add_faculty'),
  path('facutly/<int:id>', views.singleFaculty, name='single_faculty'),
  path('faculty/<int:id>/delete', views.deleteFaculty, name='delete_faculty'),
  path('all-staffs/', views.staff, name='staff'),
  path('add-staff/', views.addStaff, name='add_staff'),
  path('staff/<int:id>/delete', views.deleteStaff, name='delete_staff'),
  path('all-students/', views.student, name='student'),
  path('add-students/', views.addStudents, name='add_student'),
  path('student/<int:id>/delete', views.deleteStudent, name='delete_student'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
