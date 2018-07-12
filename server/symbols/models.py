from django.db import models

class Symbol(models.Model):
    type = models.TextField()
    symbol = models.TextField()
    slug = models.SlugField()
