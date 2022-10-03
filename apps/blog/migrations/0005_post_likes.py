# Generated by Django 4.0.4 on 2022-10-03 17:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0004_postcategory_post_blog_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(related_name="blog_post_likes", to=settings.AUTH_USER_MODEL),
        ),
    ]
