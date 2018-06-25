from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from investor.models import Investor

@receiver(post_save, sender=User)
def create_investor_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = Investor.objects.get_or_create(user=instance)
