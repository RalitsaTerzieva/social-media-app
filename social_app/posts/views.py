from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostCreateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Comment, Post


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreateForm(data=request.GET)
    return render(request,'posts/create.html',{'form':form})


def feed(request):
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post,id=post_id)
        new_comment.post = post
        new_comment.save()
    else:
        comment_form = CommentForm()
    posts = Post.objects.all()
    logged_user = request.user
    return render(request,'posts/feed.html',{'posts':posts, 'logged_user': logged_user,'comment_form':comment_form})


def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post,id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed')

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("feed")