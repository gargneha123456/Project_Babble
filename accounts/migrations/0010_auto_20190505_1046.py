# Generated by Django 2.1.2 on 2019-05-05 05:16

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('ann', '0003_auto_20190505_1008'),
        ('pll', '0006_auto_20190505_1045'),
        ('acc', '0009_remove_student_picture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='society',
            new_name='group',
        ),
    ]