# Generated by Django 4.0.4 on 2022-05-31 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediumish', '0002_remove_author_about_authorprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Story',
        ),
    ]
