# Generated by Django 4.2.10 on 2024-05-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0055_studentuser_optional_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='curriculum',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
