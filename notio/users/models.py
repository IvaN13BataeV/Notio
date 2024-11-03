from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, verbose_name='Имя')
    age = models.CharField(max_length=200, blank=True, verbose_name='Возраст')
    email = models.EmailField(max_length=200, blank=True, verbose_name='Эл.почта')
    created = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='users_images/', blank=True, verbose_name='Аватар')

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            email=user.email,
        )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
