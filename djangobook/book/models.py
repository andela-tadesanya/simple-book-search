from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,
                            unique=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"


class Book(models.Model):
    name = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=25)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "books"
