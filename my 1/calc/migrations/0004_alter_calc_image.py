# Generated by Django 4.0.1 on 2022-03-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_calc_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calc',
            name='image',
            field=models.ImageField(default='profile.png', upload_to='profile_pics'),
        ),
    ]
