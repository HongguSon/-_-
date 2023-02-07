# Generated by Django 4.1.6 on 2023-02-07 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='main/images/clothes/%Y/%m/%d')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('buying', models.TextField(blank=True, null=True)),
                ('like', models.ManyToManyField(blank=True, related_name='AccLike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bottom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='main/images/clothes/%Y/%m/%d')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('buying', models.TextField(blank=True, null=True)),
                ('like', models.ManyToManyField(blank=True, related_name='BottomLike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Outter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='main/images/clothes/%Y/%m/%d')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('buying', models.TextField(blank=True, null=True)),
                ('like', models.ManyToManyField(blank=True, related_name='OutterLike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='main/images/clothes/%Y/%m/%d')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('buying', models.TextField(blank=True, null=True)),
                ('like', models.ManyToManyField(blank=True, related_name='TopLike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(0, '공동 구매'), (1, '오픈런'), (2, '고민방')])),
                ('img', models.ImageField(blank=True, null=True, upload_to='main/images/commu/%Y/%m/%d')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='Talk_Likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='main/images/clothes/%Y/%m/%d')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('buying', models.TextField(blank=True, null=True)),
                ('like', models.ManyToManyField(blank=True, related_name='ShoesLike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(upload_to='main/images/post/%Y/%m/%d')),
                ('title', models.CharField(max_length=100)),
                ('open', models.BooleanField(default=False)),
                ('acc', models.ManyToManyField(blank=True, related_name='Acc', to='main.acc')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bottom', models.ManyToManyField(blank=True, related_name='Bottom', to='main.bottom')),
                ('likes', models.ManyToManyField(blank=True, related_name='Likes', to=settings.AUTH_USER_MODEL)),
                ('outter', models.ManyToManyField(blank=True, related_name='Outter', to='main.outter')),
                ('shose', models.ManyToManyField(blank=True, related_name='Shose', to='main.shose')),
                ('top', models.ManyToManyField(blank=True, related_name='Top', to='main.top')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('talk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.talk')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
    ]
