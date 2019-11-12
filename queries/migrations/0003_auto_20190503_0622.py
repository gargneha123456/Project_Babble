# Generated by Django 2.1.2 on 2019-05-03 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ques', '0002_auto_20190429_0717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='Branch',
        ),
        migrations.RemoveField(
            model_name='query',
            name='Society_ID',
        ),
        migrations.RemoveField(
            model_name='query',
            name='Year',
        ),
        migrations.AlterField(
            model_name='query',
            name='Subject',
            field=models.TextField(default='Academic'),
        ),
        migrations.AlterField(
            model_name='query',
            name='Timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
