# Generated by Django 4.1.7 on 2023-03-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0013_post_discounted_price_post_quantity_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='quantity_available',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subpost',
            name='quantity_available',
            field=models.IntegerField(),
        ),
    ]
