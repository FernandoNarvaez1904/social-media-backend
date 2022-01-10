from django.db import models


# Create your models here.
class Post(models.Model):
    description = models.TextField()
    publication_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now=True)

