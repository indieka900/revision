from django.urls import path
from . import views

app_name = "firstapp"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('blog/', views.blog, name="blog-page"),
    path('insert/', views.insert_data, name="insert"),
    path('details/<id>/', views.get_blog, name='details' ),
    path('update-blog/<id>/', views.update_blog, name='update-blog' ),
    path('delete-blog/<id>/', views.delete_blog, name='delete-blog' ),
]