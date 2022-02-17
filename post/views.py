from multiprocessing import context
from django.shortcuts import render

from post.models import Post

# Create your views here.
def criar_post( request ):

    context = {}

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
    return render()