from django.contrib import admin
from .models import FollowersCount, Profile, Post, Like_post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like_post)
admin.site.register(FollowersCount)
