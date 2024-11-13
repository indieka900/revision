from django.urls import path
from . import views

app_name = "firstapp"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('blog/', views.blog, name="blog-page"),
    path('insert/', views.insert_data, name="insert"),
]