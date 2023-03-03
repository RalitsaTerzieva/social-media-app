from posts import views
from posts.views import CommentDeleteView
from django.urls import path


urlpatterns = [
    path('create/',views.post_create,name='create'),
    path('feed/',views.feed,name='feed'),
    path('like/',views.like_post,name='like'),
    path("delete/<int:pk>", CommentDeleteView.as_view(template_name='posts/delete_comment.html'),name='delete'),
]