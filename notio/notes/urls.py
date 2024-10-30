from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.notes_by_category, name='notes_by_category'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('note/create/', views.note_create, name='note_form'),
    path('note/<int:note_id>/update/', views.note_update, name='note_update'),
    path('note/<int:note_id>/delete/', views.note_delete, name='note_delete'),
]