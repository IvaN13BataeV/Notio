from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='user-signup'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
