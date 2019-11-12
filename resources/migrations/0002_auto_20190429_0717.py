# Generated by Django 2.1.2 on 2019-04-29 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0007_auto_20190426_1514'),
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='Branch',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='CID',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='CR_SID',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='Year',
        ),
        migrations.AddField(
            model_name='resource',
            name='Subject',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='Timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='Uploader_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acc.student'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='Category',
            field=models.CharField(choices=[('Assignment', 'Assignment'), ('Book', 'Book PDF'), ('PPT', 'Powerpoint Presentation'), ('Question Papers', 'Question Papers')], max_length=30),
        ),
    ]
