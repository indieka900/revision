from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=60)
    auther_name = models.CharField(max_length=100)
    date_published = models.CharField(max_length=100)
    content = models.TextField()
    blog_image = models.ImageField(upload_to='blogs/')
    auther_image = models.ImageField(upload_to='authers/')
    
    
    def __str__(self):
        return self.title


# Create your models here.
