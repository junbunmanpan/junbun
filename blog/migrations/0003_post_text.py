# Generated by Django 5.1.4 on 2024-12-27 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='No content provided'),
        ),
    ]
