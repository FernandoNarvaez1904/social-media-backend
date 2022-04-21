from django.db import models

# Create your models here.
from user.models import User


class Messages(models.Model):
    creation_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    received = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
    conversation = models.ForeignKey("Conversation", related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="my_messages", on_delete=models.CASCADE)


class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name="conversations")
