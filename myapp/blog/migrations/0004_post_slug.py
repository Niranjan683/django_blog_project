# Generated by Django 5.0.6 on 2024-11-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='example-slug', unique=True),
            preserve_default=False,
        ),
    ]