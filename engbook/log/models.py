from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Logger(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    note = models.TextField(max_length=1023)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.user.username} : {self.title}'
