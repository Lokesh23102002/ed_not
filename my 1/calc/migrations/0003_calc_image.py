# Generated by Django 4.0.1 on 2022-03-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_remove_calc_h'),
    ]

    operations = [
        migrations.AddField(
            model_name='calc',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]