# Generated by Django 4.2.10 on 2024-04-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0036_dayreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayreview',
            name='school_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
