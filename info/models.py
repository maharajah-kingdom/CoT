from django.db import models

# Create your models here.

class Info(models.Model):
    text = models.CharField(max_length=999999999, blank=False)