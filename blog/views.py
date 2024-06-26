from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Post
from .forms import PostForm, CommentForm


def post_list_view(request):
    posts = Post.objects.filter(status='pub').order_by('-datetime_created')

    return render(request, 'blog/posts_list.html', {'posts': posts})


@login_required
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': post_comments,
        'comment_form': comment_form,
    })


@login_required
def post_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            return redirect(new_form)
    form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})


@login_required
def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author.id != request.user.id:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            update_form = form.save()
            return redirect(update_form)

    form = PostForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form})


@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author.id != request.user.id:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == "POST":
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_delete.html', {'post': post})
