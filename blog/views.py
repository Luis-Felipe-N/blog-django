from django.shortcuts import render
from post.models import Post

def index( request ):

    primeiro_post = Post.objects.filter(slug="minha-primeira-publicacao")

    print(  primeiro_post[0].conteudo )

    context = {
        'posts': primeiro_post
    }

    return render( request, 'index.html', context)