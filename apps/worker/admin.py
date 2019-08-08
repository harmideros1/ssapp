from django.contrib import admin
from .models import WorkerProfile, TypeId , Gender , Position, Dependence

@admin.register(WorkerProfile)
class AdminWorkerProfile(admin.ModelAdmin):
    list_display = (
        'user',
        'f_name',
        's_name',
        'l_name',
        'll_name',
        'born_date',
        'gender',
        'position',
        'type_id',
        'id_number',
        'date_in',
        'date_out',
        'active',
    )
    list_filter = ('gender', 'active',)

# @admin.register(TypeId)
class AdminTypeId(admin.ModelAdmin):
    list_display = ('id',
                    'prefix',
                    'description',
    )

# @admin.register(Gender)
class AdminGender(admin.ModelAdmin):
    list_display = ('id',
                    'prefix',
                    'description',
    )

# @admin.register(Position)
class AdminPosition(admin.ModelAdmin):
    list_display = ('id',
                    'description',
                    'dependence',
    )

# @admin.register(Dependence)
class AdminDependence(admin.ModelAdmin):
    list_display = ('id',
                    'description',
    )
    
