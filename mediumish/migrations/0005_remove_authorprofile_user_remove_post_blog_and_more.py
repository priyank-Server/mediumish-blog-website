# Generated by Django 4.0.4 on 2022-05-31 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediumish', '0004_remove_post_about_remove_post_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='relatedpost',
            name='user',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Authorprofile',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Relatedpost',
        ),
    ]