from django.db import models

# Create your models here.
from user.models import User


class Messages(models.Model):
    sender = models.ForeignKey(User, related_name="messages_sent", on_delete=models.PROTECT)
    receiver = models.ForeignKey(User, related_name="messages_received", on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    received = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)

