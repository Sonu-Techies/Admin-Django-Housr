
from django.db import models
from django.core.exceptions import ValidationError


allow_null = {"null": True, "blank": True}

# Create your models here.
class Residents(models.Model):
    """
    Model Storing detail of Resident Information
    """

    resident_name = models.CharField(
        max_length=150, blank=True, help_text="Stroring the Name of resident"
    )
    phone_number = models.CharField(
        max_length=15
    )
    resident_building_name = models.CharField(
        max_length=255, null=True, blank=True, help_text="Storing residence building name"
    )
    date_of_birth = models.DateField(**allow_null)

    rent_amount = models.DecimalField(max_digits=8, decimal_places=2)
    token_amount = models.DecimalField(max_digits=8, decimal_places=2)

    contract_start = models.DateField(**allow_null)
    contract_end_date = models.DateField(**allow_null)
    move_in_date = models.DateField(**allow_null)
    move_out_date = models.DateField(**allow_null)

    def __str__(self) -> str:
        return f"{self.resident_name} {self.contract_start} {self.contract_end_date}"
    
    def save(self, *args, **kwargs):
        if (self.contract_end_date and self.contract_start) and self.contract_end_date <= self.contract_start:
            raise ValidationError(
                'End Date can not be less than start date', 
                code='invalid_data'
            ) 
        return super().save(*args, **kwargs)
