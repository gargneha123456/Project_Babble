# Generated by Django 2.1.2 on 2019-05-07 05:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Logo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='events/'),
            preserve_default=False,
        ),
    ]
