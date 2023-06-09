from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib import admin

from core.models import TimestampedModel

class Employeer(TimestampedModel):
    """
    Model Storing detail of Employee Information
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    employee_contact_number = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the "
                "format:'+999999999'. Up to 15 digits allowed.",
            )
        ],
        null=True,
        blank=True
    )
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    @admin.display(ordering='user__last_name')
    def email(self):
        return self.user.email


    def __str__(self) -> str:
        return f"{self.user.email}"
    

    class Meta:
        ordering = ['user__first_name', 'user__last_name']