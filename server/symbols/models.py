from django.db import models

from investor.models import Investor

class Symbol(models.Model):
    type = models.CharField(max_length=16)
    symbol = models.CharField(max_length=16)
    slug = models.SlugField()
    trackers = models.ManyToManyField(Investor, symmetrical=False, blank=True, default=None)

    def __str__(self):
        return self.type + ":" + self.symbol
