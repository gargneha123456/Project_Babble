# Generated by Django 2.1.2 on 2019-05-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ques', '0005_auto_20190505_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='id',
        ),
        migrations.AlterField(
            model_name='query',
            name='Query_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]