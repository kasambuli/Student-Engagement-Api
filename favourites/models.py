from django.db import models

# Create your models here.
class Favourite(models.Model):
    article = models.ForeignKey('engagementApp.Articles', related_name='favourites')
    user_uuid = models.TextField()