# Generated by Django 4.2.10 on 2024-04-05 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculum',
            old_name='subject_name_code',
            new_name='subject_code',
        ),
        migrations.AddField(
            model_name='curriculum',
            name='subject_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
