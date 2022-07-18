from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login_page, name='login_page'),
    path('user-login', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard', views.dashboard, name='dashboard'),

    # path('Adminprofile/', views.Adminprofile, name='Adminprofile'),
    # path('people/', views.people, name='people'),
    # path('blank/', views.blank, name='blank'),
]
