# Generated by Django 4.0.1 on 2022-04-03 07:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calc', '0006_remove_calc_rans_remove_calc_rques_alter_calc_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='fields',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('guidees', models.ManyToManyField(blank=True, related_name='guidees', to=settings.AUTH_USER_MODEL)),
                ('guides', models.ManyToManyField(blank=True, related_name='guides', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='calc',
            name='fdsexpert',
            field=models.ManyToManyField(related_name='expertise_fields', to='calc.fields'),
        ),
        migrations.AddField(
            model_name='calc',
            name='fdsneeded',
            field=models.ManyToManyField(related_name='interested_fields', to='calc.fields'),
        ),
    ]
