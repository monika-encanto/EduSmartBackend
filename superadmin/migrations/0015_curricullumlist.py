# Generated by Django 4.2.10 on 2024-04-30 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0014_alter_announcement_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurricullumList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum_name', models.CharField(max_length=255)),
                ('class_name', models.CharField(max_length=255)),
                ('class_subject', models.JSONField()),
            ],
        ),
    ]
