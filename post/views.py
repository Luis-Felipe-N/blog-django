from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from post.forms import PostForm

from post.models import Post

# Create your views here.
def criar_post(request):

    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)

            post.data_publicado = timezone.now()

            post.save()

            redirect(f'posts')

    context = {
        "form": form
    }

    return render(request, "criar.html", context)

def exibir_posts_por_categoria(request, categoria):

    posts = Post.objects.filter(categoria=categoria)
    quantidade_posts = len(posts)

    context = {
        "categoria": categoria,
        "posts": posts,
        "quantidade_posts": quantidade_posts
    }

    return render(request, "posts.html", context)

def exibir_post_por_slug(request, slug):

    post = get_object_or_404( Post, slug=slug )

    context = {
        "post": post
    }

    return render(request, "index.html", context)