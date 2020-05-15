from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.text import slugify
# Create your models here.


class Teams(models.Model):
    """
    Teams for Capstone Project
    Profanity Check
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    members = models.ManyToManyField(User)
    token = models.UUIDField(
        primary_key=True, default=uuid.uuid4)  # email joining
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Teams, self).save(*args, **kwargs)

    def checkMembers(self):
        """
        Query to check wether there are less than 2 members on the group
        """
        if (1):
            return True
        else:
            return ValidationError(" Less 2 Memebers not Allowed")


class Project(models.Model):
    """
        Project Models 
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'{self.user.username} : {self.title}'
