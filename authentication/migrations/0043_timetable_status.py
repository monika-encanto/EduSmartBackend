# Generated by Django 4.2.10 on 2024-04-25 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0042_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='status',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
