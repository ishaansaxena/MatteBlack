from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db import models

class Investor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username
