# Generated by Django 4.2.10 on 2024-05-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0050_eventscalender_school_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventscalender',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='eventscalender',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
