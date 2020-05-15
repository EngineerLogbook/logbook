from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.text import slugify
# Create your models here.


class Team(models.Model):
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
    published = models.BooleanField(default=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        """
        Return Name
        """
        return f'{self.name}'

    def save(self, *args, **kwargs):
        # Slugify the name for the URL
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def checkMembers(self):
        """
        Query to check wether there are less than 2 members on the group
        """
        if (1):
            return True
        else:
            return ValidationError(" Less 2 Members not Allowed")

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


class Project(models.Model):
    """
        Project Models 
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    access_token = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)

    description = models.TextField(max_length=512)
    date_started = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='project_header', null=True)
    logo = models.ImageField(upload_to='project_logo', null=True)

    slug = models.SlugField(max_length=255)
    published = models.BooleanField(default=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} : {self.title}'

    def save(self, *args, **kwargs):
        # Slugify the name for the URL
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

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
