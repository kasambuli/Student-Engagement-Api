from django.conf import settings
from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=40)
    Content = models.TextField()
    # image = models.ImageField()
    category = models.CharField(max_length=40)
    author = models.CharField(max_length=40)

    def __str__(self):
        return self.title 