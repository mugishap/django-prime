from distutils.command.upload import upload
from django.db import models
from traitlets import default

# Create your models here.

class Profile(models.Model):
    user = 'pass'
    user_id = 'pass'
    bio = 'pass'
    profileimg = models.ImageField(upload_to = 'profile_images',default='profile_picture.png')
    location = 'pass'
