# Generated by Django 4.2.10 on 2024-04-30 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0046_teachersschedule_school_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='guardian_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
