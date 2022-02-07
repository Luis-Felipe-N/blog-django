# Generated by Django 4.0.2 on 2022-02-06 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=194)),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('categoria', models.CharField(choices=[('django', 'django'), ('python', 'python')], default='django', max_length=6, verbose_name='Opções')),
                ('slug', models.CharField(max_length=194, verbose_name='Slug')),
                ('data_publicado', models.DateTimeField(auto_now_add=True, verbose_name='Data de publicação')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'post',
            },
        ),
    ]
