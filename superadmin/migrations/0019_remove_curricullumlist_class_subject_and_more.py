# Generated by Django 4.2.10 on 2024-05-04 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0018_subjects_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curricullumlist',
            name='class_subject',
        ),
        migrations.RemoveField(
            model_name='curricullumlist',
            name='optional_subject',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='subject_name',
        ),
        migrations.AddField(
            model_name='subjects',
            name='curriculum_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='superadmin.curricullumlist'),
        ),
        migrations.AddField(
            model_name='subjects',
            name='optional_subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='primary_subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='curricullumlist',
            name='class_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Classes',
        ),
    ]
