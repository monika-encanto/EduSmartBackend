from django.db import models

from EduSmart import storage_backends
from curriculum.models import Curriculum, Subjects, Classes
from constants import CONTENT_TYPES

class Content(models.Model):
    school_id = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='', blank=True, null=True, storage=storage_backends.AzureMediaStorage(azure_container='image'))
    content_media = models.FileField(upload_to='content/', blank=True, null=True)
    content_media_link = models.URLField(max_length=1024, blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    content_name = models.CharField(max_length=255)
    content_creator = models.CharField(max_length=255, blank=True, null=True)
    curriculum = models.CharField(max_length=255, blank=True, null=True)
    classes = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    supporting_detail = models.TextField(blank=True, null=True)
    description = models.TextField()
    is_recommended = models.BooleanField(default=False)
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.id}'

    @property
    def is_generic(self):
        return self.subject is None
