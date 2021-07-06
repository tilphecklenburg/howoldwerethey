from django.db import models
from .tools import getcelebrityage

class Celebrity(models.Model):
    name = models.CharField(max_length=30, default='')
    age = models.CharField(max_length=3, default='10')

    def __str__(self):
        return self.name


class Media(models.Model):
    mediatitle = models.CharField(max_length=30, default='notitle')
    characters = models.ForeignKey(Celebrity, on_delete=models.CASCADE, default='no characters')

    def __str__(self):
        return self.mediatitle
