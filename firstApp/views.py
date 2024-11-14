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

#CRUD

#Fuction to retrieve one item
def get_blog(request, id):
    blog = Blog.objects.get(pk=id)
    return render(request, 'details.html', {'blg' : blog})

#update function
def update_blog(request, id):
    blog = Blog.objects.get(pk=id)
    if request.method == 'POST':
        # getting the new values
        title = request.POST['title']
        ctgry = request.POST['category']
        auther_name = request.POST['auther_name']
        date_published = request.POST['date_published']
        content = request.POST['content']
        auther_image = request.FILES['author_image']
        blog_image = request.FILES['blog_image']
        
        # equating the new values to the existing blog
        blog.title = title
        blog.category = ctgry
        blog.auther_name = auther_name
        blog.date_published = date_published
        blog.content = content
        blog.auther_image = auther_image
        blog.blog_image = blog_image
        
        # saving the blog
        blog.save()
        
        # redirect to homapage
        return redirect('/')
    return render(request, 'update_blog.html', {'blog' : blog})

def delete_blog(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('/')

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
