# Generated by Django 2.1.2 on 2019-05-05 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ann', '0007_auto_20190505_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='CR_ID',
            new_name='CR',
        ),
    ]