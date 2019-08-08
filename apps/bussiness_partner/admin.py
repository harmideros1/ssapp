from django.contrib import admin
from .models import BussinessPartner, Address, Zone

@admin.register(BussinessPartner)
class AdminBussinessPartner(admin.ModelAdmin):
    list_display = (
        'code', 
        'f_name', 
        's_name', 
        'l_name', 
        'll_name', 
        'employe', 
        # 'address', 
        'phone', 
        'state', 
    )
@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = (
        'address', 
        'zone', 
    )

@admin.register(Zone)
class AdminZone(admin.ModelAdmin):
    list_display = (
        'code', 
        'description', 
    )
