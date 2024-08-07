from django.contrib.auth.hashers import make_password
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from EduSmart import storage_backends
from authentication.models import User


# Create your models here.


class SchoolProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to='', blank=True, storage=storage_backends.AzureMediaStorage(azure_container='image'))
    school_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=200,null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    established_year = models.IntegerField(null=True, blank=True)
    school_type = models.CharField(max_length=255, null=True, blank=True)
    principle_name = models.CharField(max_length=255, null=True, blank=True)
    contact_no = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    school_website = models.CharField(max_length=255, null=True, blank=True)
    school_id = models.CharField(max_length=200, null=True, blank=True)
    contract = models.FileField(upload_to='', null=True, blank=True, storage=storage_backends.AzureMediaStorage(azure_container='file'))
    description = models.TextField(null=True, blank=True)


class SchoolProfilePassword(models.Model):
    school = models.ForeignKey(SchoolProfile, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)


class Announcement(models.Model):
    creator_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, default="super admin")
    date_time = models.DateTimeField(auto_now=True)
    announcement_title = models.CharField(max_length=255)
    description = models.TextField()


class CurricullumList(models.Model):
    curriculum_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Subjects(models.Model):
    school_id = models.CharField(max_length=255)
    curriculum_id = models.ForeignKey(CurricullumList, on_delete=models.CASCADE, blank=True, null=True)
    primary_subject = models.CharField(max_length=255, blank=True, null=True)
    optional_subject = models.CharField(max_length=255, blank=True, null=True)