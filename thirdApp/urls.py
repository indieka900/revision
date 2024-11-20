from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.user_registration, name='register'),
    path('sign-in/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]