"""
URL configuration for notio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('notes/', views.note_list, name='note_list'),
    path('<int:note_id>/', views.note_detail, name='note_detail'),
    path('create/', views.note_create, name='note_create'),
    path('<int:note_id>/update/', views.note_update, name='note_update'),
    path('<int:note_id>/delete/', views.note_delete, name='note_delete'),
]
