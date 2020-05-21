from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    "Model representing a message as part of a messaging system"
    
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name="receiver")
    message = models.TextField()
    subject = models.CharField(max_length=80)
    creation_date = models.DateField(default=datetime.today())
    unread = models.BooleanField(default=True)