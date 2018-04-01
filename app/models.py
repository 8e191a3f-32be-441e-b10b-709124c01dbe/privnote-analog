import uuid
from django.db import models
from django.utils import timezone

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    fire_date = models.DateTimeField(blank=True, null=True)
    