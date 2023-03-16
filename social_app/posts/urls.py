from posts import views
from django.urls import path


urlpatterns = [
    path('create/',views.post_create,name='create'),
    path('feed/',views.feed,name='feed'),
]