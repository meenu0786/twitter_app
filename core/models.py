from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
