# Generated by Django 2.1.2 on 2019-05-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0019_auto_20190505_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Picture',
            field=models.ImageField(default='/quer', upload_to='balk'),
            preserve_default=False,
        ),
    ]
