# Generated by Django 2.1.2 on 2019-04-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0006_remove_student_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
