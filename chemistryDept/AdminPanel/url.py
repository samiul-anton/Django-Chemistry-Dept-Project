from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('user-login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('people/', include('peopleApp.url')),
    path('research/', include('researchApp.url')),
    path('resource/', include('resourceApp.url')),
    path('events/', include('eventsApp.url')),
]
