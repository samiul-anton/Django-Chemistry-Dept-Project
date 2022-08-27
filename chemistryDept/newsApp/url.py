from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  #news url
  path('', views.allNews, name='all_news'),
  path('add-news/', views.addNews, name='add_news'),
  # path('edit-faculty/<int:id>', views.editFaculty, name='edit_faculty'),
  # path('facutly/<int:id>', views.singleFaculty, name='single_faculty'),
  # path('faculty/getData/<int:id>', views.facultyGetdata, name='get_data'),
  # path('faculty/<int:id>/delete', views.deleteFaculty, name='delete_faculty'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
