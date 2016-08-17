from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,
                            unique=True)


class Book(models.Model):
    name = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=25)
    category = models.ForeignKey(Category)
