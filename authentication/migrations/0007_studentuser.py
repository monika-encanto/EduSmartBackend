# Generated by Django 4.2.10 on 2024-03-13 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_teacheruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('father_name', models.CharField(max_length=150)),
                ('mother_name', models.CharField(max_length=150)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=50)),
                ('father_occupation', models.CharField(max_length=255)),
                ('admission_date', models.DateField(auto_now_add=True, null=True)),
                ('school_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('bus_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('canteen_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('other_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('religion', models.CharField(choices=[('christian', 'Christian'), ('islam', 'Islam'), ('hinduism', 'Hinduism'), ('buddhism', 'Buddhism'), ('sikhism', 'Sikhism'), ('judaism', 'Judaism'), ('other', 'Other')], max_length=50)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=50)),
                ('class_enrolled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.class')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
