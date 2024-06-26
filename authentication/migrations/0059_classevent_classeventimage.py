# Generated by Django 4.2.10 on 2024-05-10 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0058_timetable_curriculum'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.CharField(blank=True, max_length=255, null=True)),
                ('curriculum', models.CharField(blank=True, max_length=255, null=True)),
                ('select_class', models.CharField(max_length=255)),
                ('section', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('title', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassEventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.FileField(upload_to='class_event_image/')),
                ('class_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_event_image', to='authentication.classevent')),
            ],
        ),
    ]
