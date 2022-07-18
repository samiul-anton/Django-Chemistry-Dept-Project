from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  path('faculty/', views.faculty, name='faculty'),
  path('staff/', views.staff, name='staff'),
  path('student/', views.student, name='student'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
