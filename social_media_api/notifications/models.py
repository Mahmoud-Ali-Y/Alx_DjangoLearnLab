from django.db import models
from accounts.models import CustomUser
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    verb = models.CharField(max_length=200)
    target = GenericForeignKey("content_type", "object_id")
    timestamp = models.DateTimeField(auto_now_add=True)