from django.contrib import admin
from .models import WorkOrderAssignment

@admin.register(WorkOrderAssignment)
class AdminBussinessPartner(admin.ModelAdmin):
    list_display = (
        'client', 
        'address',
        'description', 
        'technician', 
        'date', 
    )
