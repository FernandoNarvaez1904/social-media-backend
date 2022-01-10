from django.db import models
from django.utils.timezone import now

# Create your models here.
from user.models import User


class Post(models.Model):
    description = models.TextField()
    publication_date = models.DateTimeField(default=now, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="my_posts", on_delete=models.PROTECT)
