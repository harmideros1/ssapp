from django.db import models
from apps.bussiness_partner.models import BussinessPartner
from django.conf import settings

class Motive(models.Model):
    code = models.CharField(max_length=50, verbose_name="Código", primary_key=True)
    description = models.CharField(max_length=50, verbose_name="Descripción", )

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Motivo"
        verbose_name_plural = "Motivos"

class WorkOrder(models.Model):
    reference = models.DecimalField(max_digits=7, verbose_name="Referencia Nº", decimal_places=0)
    client = models.ForeignKey(BussinessPartner, verbose_name="Cliente",  on_delete=models.PROTECT)
    address = models.CharField(max_length=50, verbose_name="Dirección", )
    motive = models.ForeignKey(Motive, verbose_name="Motivo", on_delete=models.PROTECT)
    work_done = models.TextField(verbose_name="Trabajo realizado", )
    pending_job = models.TextField(verbose_name="Trabajo pendiente", null=True, blank=True)
    request_quote = models.BooleanField(verbose_name="¿Solicita cotización?", )
    problem_solved = models.BooleanField(verbose_name="¿Problema técnico solucionado?", )
    start_job = models.DateTimeField(verbose_name="Hora entrada", )
    end_job = models.DateTimeField(verbose_name="Hora salida", )
    # technician = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Técnico", on_delete=models.PROTECT)
    technician = models.ForeignKey('auth.User', verbose_name="Técnico", on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.reference)

    class Meta:
        verbose_name = 'Orden de trabajo y/o suministro'
        verbose_name_plural = 'Ordenes de trabajo y/o suministro'
