# Generated by Django 4.2.10 on 2024-05-01 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0049_merge_20240501_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventscalender',
            name='school_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='eventscalender',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventscalender',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
