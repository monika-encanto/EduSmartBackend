# Generated by Django 4.2.10 on 2024-04-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_alter_studentuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='subject',
            field=models.CharField(default='[]', max_length=1000),
        ),
    ]
