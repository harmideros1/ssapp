from django.contrib import admin
from .models import WorkOrder, Motive

@admin.register(WorkOrder)
class AdminWorkOrder(admin.ModelAdmin):
    list_display = (
        'reference',
        'client',
        'address',
        'motive',
        'work_done',
        'pending_job',
        'request_quote',
        'problem_solved',
        'start_job',
        'end_job',
        'technician',
        'date',
    )

# @admin.register(Motive)
class AdminMotive(admin.ModelAdmin):
    list_display = (
        'code',
        'description',
    )