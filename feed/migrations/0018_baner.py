# Generated by Django 4.1.7 on 2023-03-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0017_alter_post_quantity_available_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='subpost')),
            ],
        ),
    ]
