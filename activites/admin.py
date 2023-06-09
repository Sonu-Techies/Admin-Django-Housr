from django.contrib import admin

# Register your models here.
from django.contrib import admin
from activites.models import CommunityEvents

# Register your models here.
@admin.register(CommunityEvents)
class CommunityEventsAdmin(admin.ModelAdmin):
    list_display = [
        'event_name', 
        'event_date',  
        'event_description',
        'employee'
    ]
    list_filter = ['employee']
    list_per_page = 10