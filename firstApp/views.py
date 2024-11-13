from django.shortcuts import render, redirect
from firstApp.models import Blog


def home(request):
    title = "Joseph's Web"
    blogs = Blog.objects.all()
    context = {
        'project_title' : title,
        'blogs' : blogs
    }
    return render(request, 'index.html', context)

def insert_data(request):
    if request.method == 'POST':
        title = request.POST['title']
        ctgry = request.POST['category']
        auther_name = request.POST['auther_name']
        date_published = request.POST['date_published']
        content = request.POST['content']
        auther_image = request.FILES['author_image']
        blog_image = request.FILES['blog_image']
        blog = Blog(
            title = title,
            category = ctgry,
            auther_name = auther_name,
            date_published = date_published,
            content = content,
            blog_image = blog_image,
            auther_image = auther_image
        )
        blog.save()
        redirect('firstapp:homepage')
        
    return render(request, 'insert.html')

def blog(request):
    title = "Joseph's Web"
    context = {
        'project_title' : title
    }
    return render(request, 'blog.html', context)

# Create your views here.
