from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    age = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='users_images', blank=True)

    def __str__(self):
        return self.name
