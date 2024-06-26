# Generated by Django 4.2.10 on 2024-04-09 10:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('school_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('established_year', models.IntegerField()),
                ('school_type', models.CharField(max_length=255)),
                ('principle_name', models.CharField(max_length=255)),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('school_website', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
