from django.db import models
from django.contrib.auth.models import User
import uuid
from project.models import Team, Project
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# Create your models here.


class DesignBaseClass(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=127)
    slug = models.SlugField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        # Slugify the name for the URL
        self.slug = slugify(self.name)
        super(DesignBaseClass, self).save(*args, **kwargs)

    def publishedFlip(self, *args, **kwargs):
        """
        Published Flip Switch
        """
        self.published = not self.published
        try:
            self.save(*args, **kwargs)
        except:
            ValidationError("Internal Server Error")

    def reviewFlip(self, *args, **kwargs):
        """
        Published revied Flip
        """
        self.reviewed = not self.reviewed
        try:
            self.save(*args, **kwargs)
        except:
            ValidationError("Internal Server Error")


class Logger(DesignBaseClass):

    note = models.TextField(max_length=1023)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    date_modified = models.DateTimeField(null=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return f'{self.user.username} : {self.title}'


class LogFile(DesignBaseClass):
    FILE_TYPES = [
        ("image", "image"),
        ("pdf", "pdf"),
        ("dwg", "dwg"),
        ("misc", "misc")
    ]

    file = models.FileField(upload_to="logfile")
    filetype = models.CharField(max_length=100, choices=FILE_TYPES)
