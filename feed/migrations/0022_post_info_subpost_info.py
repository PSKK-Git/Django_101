# Generated by Django 4.1.7 on 2023-04-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0021_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='info',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subpost',
            name='info',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]