# Generated by Django 2.1.2 on 2019-05-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20190429_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('SID', models.AutoField(primary_key=True, serialize=False)),
                ('Subject_Code', models.CharField(max_length=6)),
                ('Name', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='resource',
            name='Category',
            field=models.CharField(choices=[('Assignment', 'Assignment'), ('Book', 'Book PDF'), ('PPT', 'Powerpoint Presentation'), ('Question Papers', 'Question Papers')], max_length=50),
        ),
    ]
