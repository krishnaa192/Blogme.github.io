# Generated by Django 3.2.12 on 2023-01-09 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0013_alter_blog_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
    ]
