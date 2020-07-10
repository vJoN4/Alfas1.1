from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

def user_directory_path(instance, filename):
    return '/'.join(['profile_pictures/', instance.username+'.jpg'])

class User(AbstractUser):
    foto = models.ImageField(upload_to=user_directory_path, default='default.jpg', blank=True, null=True)