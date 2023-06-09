from django.db import models
from employee.models import Employeer
# Create your models here.

class CommunityEvents(models.Model):
    """
    Store Event Details
    """

    event_name = models.CharField(
        max_length=150, help_text="Store Event Details"
    )
    event_date = models.DateTimeField(
        auto_now_add=True
    )
    event_description = models.TextField(
        blank=True, null=True
    )

    employee = models.ForeignKey(
        Employeer,
        on_delete=models.DO_NOTHING,
    )
    
