from django.db import models
from django.contrib.auth.models import User
from notes.models import Note


# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, blank=True)
#     email = models.EmailField(max_length=200, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
