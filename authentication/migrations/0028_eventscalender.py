# Generated by Django 4.2.10 on 2024-04-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0027_rename_teacher_staffattendence_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsCalender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_event', models.CharField(max_length=200)),
                ('event_date', models.DateField()),
                ('calendar', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('event_image', models.ImageField(blank=True, upload_to='')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
