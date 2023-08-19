from django.contrib import admin
from .models import Opportunity, Shelter
# Register your models here.

class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'gender', 'shelter', 'type', 'date_created']

class ShelterAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state']
    
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Shelter, ShelterAdmin)