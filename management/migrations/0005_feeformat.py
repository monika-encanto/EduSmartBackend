# Generated by Django 4.2.10 on 2024-07-09 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_fee_salary_school_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(blank=True, max_length=255, null=True)),
                ('field_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('fee_structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fee_structure', to='management.fee')),
            ],
        ),
    ]
