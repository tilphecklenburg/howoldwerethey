from django.db import models
from tools import getcelebrityage

class Celebrity(models.Model):
    age = models.CharField(max_length=3)
    #placeholder for celebrity class/db table

class Media(models.Model):
    mediatitle = models.CharField(max_length=3)