# Generated by Django 4.0.1 on 2022-05-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0010_calc_guide_rating_calc_guidee_rating_calc_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='calc',
            name='certificates',
            field=models.ManyToManyField(blank=True, to='calc.certificates'),
        ),
    ]