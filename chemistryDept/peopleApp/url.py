from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  #faculty url
  path('all-facultys/', views.faculty, name='faculty'),
  path('add-faculty/', views.addFaculty, name='add_faculty'),
  path('edit-faculty/<int:id>', views.editFaculty, name='edit_faculty'),
  path('facutly/<int:id>', views.singleFaculty, name='single_faculty'),
  path('faculty/getData/<int:id>', views.facultyGetdata, name='get_data'),
  path('faculty/<int:id>/delete', views.deleteFaculty, name='delete_faculty'),
  #staff urls
  path('all-staffs/', views.staff, name='staff'),
  path('staff/getData/<int:id>', views.staffGetdata, name='get_data_staff'),
  path('edit-staff/<int:id>', views.editStaff, name='edit_staff'),
  path('add-staff/', views.addStaff, name='add_staff'),
  path('staff/<int:id>/delete', views.deleteStaff, name='delete_staff'),
  #student urls
  path('all-students/', views.student, name='student'),
  path('student/getData/<int:id>', views.studentGetdata, name='get_data_student'),
  path('add-students/', views.addStudents, name='add_student'),
  path('student/<int:id>/delete', views.deleteStudent, name='delete_student'),
  path('edit-student/<int:id>', views.editStudent, name='edit_student'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
