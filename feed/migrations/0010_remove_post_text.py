# Generated by Django 4.1.7 on 2023-03-19 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_post_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]
