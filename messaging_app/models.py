from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name="receiver")
    message = models.TextField()
    subject = models.CharField(max_length=80)
    creation_date = models.DateField()
    unread = models.BooleanField()