# Generated by Django 4.0.1 on 2022-06-14 16:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0008_alter_guideinfo_lastgdelstseen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guideinfo',
            name='lastgdelstseen',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 16, 57, 47, 599390, tzinfo=utc)),
        ),
    ]
