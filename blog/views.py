from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post


def post_list_view(request):
    posts_list = Post.objects.filter(status='pub').order_by('datetime_modified')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new_view(request):
    if request.method == "POST":
        post_text = request.POST.get('title')
        post_title = request.POST.get('text')
        Post.objects.create(title=post_title, text=post_text,
                            author=None, stauts='pub')
    else:
        return render(request, 'blog/post_create.html')
