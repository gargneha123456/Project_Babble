# Generated by Django 2.1.2 on 2019-05-07 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_auto_20190507_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='Subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.subject'),
        ),
    ]