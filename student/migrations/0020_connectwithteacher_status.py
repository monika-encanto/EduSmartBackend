# Generated by Django 4.2.10 on 2024-05-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_connectwithteacher_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectwithteacher',
            name='status',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
