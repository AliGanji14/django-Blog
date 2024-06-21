from django.views import generic
from django.urls import reverse_lazy


from .models import Post
from .forms import PostForm


class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ['title', 'text', 'status']
    template_name = 'blog/post_update.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
