from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.
class Post( models.Model ):
    titulo = models.CharField(
        max_length=194,
        verbose_name="Título"
    )

    conteudo = models.TextField(
        verbose_name="Conteúdo"
    )

    categoria = models.CharField(
        choices=[
            ('django', 'django'),
            ('python', 'python')
            ],
        default='django',
        verbose_name="Categoria",
        max_length=6
    )

    slug = models.CharField(
        verbose_name="Slug",
        max_length=194,
        blank=False,
    )

    data_publicado = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de publicação"
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "post"

    def __str__(self):
        return self.titulo