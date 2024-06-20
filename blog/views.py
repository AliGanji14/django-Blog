from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Post
from .forms import NewPostForm


def post_list_view(request):
    posts_list = Post.objects.filter(
        status='pub').order_by('datetime_modified')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new_view(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = NewPostForm()
    return render(request, 'blog/post_create.html', {'form': form})
