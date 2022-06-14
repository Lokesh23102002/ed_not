# Generated by Django 4.0.1 on 2022-06-11 04:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import guide.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calc', '0018_rating_review_remove_usrinfo_certificates_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuedby', models.CharField(blank=True, max_length=500)),
                ('certificate', models.FileField(blank=True, upload_to=guide.models.user_directory_path)),
                ('fd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.fields')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='guideinfo',
            fields=[
                ('usr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rating', models.FloatField(default=0.0)),
                ('level', models.IntegerField(default=0)),
                ('connectmode', models.IntegerField(default=0)),
                ('lastgdelstseen', models.DateTimeField(default=datetime.datetime(2022, 6, 11, 4, 51, 59, 355206, tzinfo=utc))),
                ('certificates', models.ManyToManyField(blank=True, to='guide.Certificate')),
                ('fds', models.ManyToManyField(blank=True, related_name='expertise_fields', to='calc.fields')),
                ('guide_rooms', models.ManyToManyField(blank=True, related_name='guide_rooms', to='chat.room')),
                ('questions_byguidees', models.ManyToManyField(blank=True, related_name='questions_byguidees', to='calc.Question')),
                ('ratings_given', models.ManyToManyField(blank=True, related_name='guide_rated', to='calc.Rating')),
                ('ratings_received', models.ManyToManyField(blank=True, related_name='guide_received', to='calc.Rating')),
                ('rvws_posted', models.ManyToManyField(blank=True, related_name='reviews_posted_bygd', to='calc.Review')),
                ('rvws_received', models.ManyToManyField(blank=True, related_name='reviews_received_bygd', to='calc.Review')),
            ],
        ),
    ]