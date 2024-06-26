# Generated by Django 4.2.10 on 2024-05-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_content_is_recommended'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='student_images/'),
        ),
        migrations.AlterField(
            model_name='content',
            name='classes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='curriculum',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
