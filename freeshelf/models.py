from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    description = models.TextField()
    slug=models.SlugField(unique=True)
    date = models.DateField()
    url = models.URLField()
