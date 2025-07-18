from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_post_list, name='public_post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),]