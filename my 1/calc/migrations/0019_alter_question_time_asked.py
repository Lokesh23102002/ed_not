# Generated by Django 4.0.1 on 2022-06-11 05:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0018_rating_review_remove_usrinfo_certificates_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='time_asked',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 5, 20, 17, 442047, tzinfo=utc)),
        ),
    ]
