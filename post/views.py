from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from post.forms import PostForm

from post.models import Post

# Create your views here.
def criar_post(request):

    form = PostForm()

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