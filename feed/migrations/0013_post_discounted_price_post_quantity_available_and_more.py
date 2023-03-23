# Generated by Django 4.1.7 on 2023-03-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_alter_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='post',
            name='quantity_available',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subpost',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='subpost',
            name='quantity_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subpost',
            name='type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='subpost'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
