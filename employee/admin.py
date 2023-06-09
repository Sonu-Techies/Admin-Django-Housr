from datetime import datetime
# from dateutil.relativedelta import relativedelta

from django.contrib import admin

from .models import Employeer


@admin.register(Employeer)
class EmployeeAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['first_name', 'last_name',  'email']
    list_filter = ['user__username']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
