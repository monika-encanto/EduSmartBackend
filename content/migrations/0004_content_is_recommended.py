# Generated by Django 4.2.10 on 2024-05-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_content_school_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='is_recommended',
            field=models.BooleanField(default=False),
        ),
    ]
