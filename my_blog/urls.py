from django.contrib import admin
from django.urls import path
from blog.views import index
from post.views import criar_post, exibir_post_por_slug, exibir_posts_por_categoria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('criar-post', criar_post, name="criar_post"),
    path('posts/<str:categoria>', exibir_posts_por_categoria, name="exibir_post_por_categoria"),
    path('post/<str:slug>', exibir_post_por_slug, name="exibir_post_por_slug")
]
