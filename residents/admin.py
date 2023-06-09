from django.contrib import admin
from residents.models import Residents

# Register your models here.
@admin.register(Residents)
class ResidentsAdmin(admin.ModelAdmin):
    list_display = [
        'resident_name', 
        'phone_number',  
        'resident_building_name', 'rent_amount', 'token_amount', 
        'contract_start', 'contract_end_date', 
        'move_in_date', 'move_out_date'
    ]
    list_filter = ['resident_name']
    list_per_page = 10

    ordering = ['contract_start', 'contract_end_date']
    search_fields = ['resident_name__istartswith']