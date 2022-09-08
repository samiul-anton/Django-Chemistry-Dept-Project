from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  #news url
  path('', views.allNews, name='all_news'),
  path('add-news/', views.addNews, name='add_news'),
  path('edit-news/<int:id>', views.editNews, name='edit_news'),
  path('getData/<int:id>', views.newsGetdata, name='get_news_data'),
  path('news/<int:id>/delete', views.deleteNews, name='delete_news'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
