# Generated by Django 4.2.10 on 2024-04-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0035_alter_user_school_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
