from django.db import models
from django.contrib.auth.models import AbstractUser
from core.constant import UserType
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class User(AbstractUser):
    """
    Override Abstract user for adding user type
    """
    email = models.EmailField(unique=True)

    user_type = models.CharField(
        max_length=8, 
        choices=list(UserType), 
        default=UserType.EMPLOYEE
    )
