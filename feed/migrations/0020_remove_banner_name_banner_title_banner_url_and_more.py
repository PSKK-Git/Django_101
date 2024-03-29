# Generated by Django 4.1.7 on 2023-03-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0019_alter_baner_image_alter_post_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='name',
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banners/'),
        ),
    ]
