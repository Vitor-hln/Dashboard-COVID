from django.contrib import admin
from .models import Country, CovidData, VaccineApproval

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'population']
    search_fields = ['name', 'code']

@admin.register(CovidData)
class CovidDataAdmin(admin.ModelAdmin):
    list_display = ['country', 'date', 'total_cases', 'total_deaths']
    list_filter = ['country', 'date']
    search_fields = ['country__name']
    date_hierarchy = 'date'

@admin.register(VaccineApproval)
class VaccineApprovalAdmin(admin.ModelAdmin):
    list_display = ['country', 'vaccine_name', 'approval_date']
    list_filter = ['country', 'approval_date']
    search_fields = ['country__name', 'vaccine_name']