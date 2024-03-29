# Generated by Django 4.2.10 on 2024-03-13 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_payrollmanagementuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=10)),
                ('is_default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
