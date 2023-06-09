from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import User
from employee.models import Employeer

@receiver(post_save, sender=User)
def create_offers(instance, **kwargs):
    if kwargs["created"]:
        Employeer.objects.create(
            user=instance,
        )

