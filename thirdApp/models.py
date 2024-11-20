from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=35)
    description = models.TextField()
    profile_pic = models.FileField(upload_to='teams/')
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)
    linkedin_url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} --- {self.position}"
    
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='users/', default='profile.png')