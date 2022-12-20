from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload, name= 'upload'),
    path('like_post', views.like_post, name= 'like-post'),
]
