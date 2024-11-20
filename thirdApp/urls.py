from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.user_registration, name='sign-up')
]