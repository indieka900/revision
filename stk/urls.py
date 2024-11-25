from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-s'),
    path('checkout', views.checkout, name='checkout'),
    path('stk/', views.stk, name='stk-push')
]