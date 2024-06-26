# Generated by Django 4.2.10 on 2024-04-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_alter_teacheruser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacheruser',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='highest_qualification',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
