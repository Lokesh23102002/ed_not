# Generated by Django 4.0.1 on 2022-06-11 05:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_alter_guideinfo_lastgdelstseen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate',
            field=models.FileField(blank=True, upload_to='certificates'),
        ),
        migrations.AlterField(
            model_name='guideinfo',
            name='lastgdelstseen',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 5, 22, 50, 336650, tzinfo=utc)),
        ),
    ]
