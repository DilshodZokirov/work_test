from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.


class SubjectLesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos_uploaded', null=False,
                             validators=[
                                 FileExtensionValidator(
                                     allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv']
                                 )]
                             )
    category_id = models.CharField(max_length=200)
