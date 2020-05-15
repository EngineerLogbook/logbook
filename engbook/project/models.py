from django.db import models
import uuid
from django.contrib.auth.models import User

from django.utils.text import slugify
from log.models import DesignBaseClass
# Create your models here.


class Team(DesignBaseClass):
    """
    Teams for Capstone Project Profanity Check
    """
    description = models.CharField(max_length=255)
    members = models.ManyToManyField(User)
    token = models.UUIDField(
        primary_key=True, default=uuid.uuid4)  # email joining

    def checkMembers(self):
        """
        Query to check wether there are less than 2 members on the group
        """
        if (1):
            return True
        else:
            return ValidationError(" Less 2 Members not Allowed")


class Project(DesignBaseClass):
    """
        Project Models 
    """

    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    access_token = models.UUIDField(
        primary_key=True, default=uuid.uuid4)

    description = models.TextField(max_length=512)

    image = models.ImageField(upload_to='project_header', null=True)
    logo = models.ImageField(upload_to='project_logo', null=True)
