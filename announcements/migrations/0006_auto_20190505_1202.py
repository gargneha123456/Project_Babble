# Generated by Django 2.1.2 on 2019-05-05 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ann', '0005_auto_20190505_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='CID',
            new_name='GID',
        ),
    ]