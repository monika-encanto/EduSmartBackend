# Generated by Django 4.2.10 on 2024-05-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0005_curriculum_school_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculum',
            old_name='subject_name_code',
            new_name='optional_subject',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='exam_board',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='section',
        ),
        migrations.AddField(
            model_name='curriculum',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='primary_subject',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='select_class',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='syllabus',
            field=models.FileField(blank=True, null=True, upload_to='syllabus/'),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='curriculum_name',
            field=models.JSONField(default=list),
        ),
    ]
