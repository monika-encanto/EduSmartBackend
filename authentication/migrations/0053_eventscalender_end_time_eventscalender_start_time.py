# Generated by Django 4.2.10 on 2024-05-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0052_remove_eventscalender_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventscalender',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='eventscalender',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
