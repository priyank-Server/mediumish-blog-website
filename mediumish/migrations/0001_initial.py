# Generated by Django 4.0.4 on 2022-05-30 10:55

import ckeditor.fields
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
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='Story', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relatedpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='Relatedpost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(default=True, upload_to='')),
                ('description', ckeditor.fields.RichTextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='Blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(default=True, upload_to='')),
                ('description', models.TextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]