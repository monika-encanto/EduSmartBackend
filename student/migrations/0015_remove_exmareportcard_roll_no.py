# Generated by Django 4.2.10 on 2024-05-07 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_zoomlink_curriculum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exmareportcard',
            name='roll_no',
        ),
    ]