from django.db import models
from apps.bussiness_partner.models import BussinessPartner
from apps.worker.models import WorkerProfile
from django.conf import settings

class WorkOrderAssignment(models.Model):

    client = models.ForeignKey(BussinessPartner, verbose_name="Cliente", on_delete=models.PROTECT)
    address = models.CharField(max_length=200, verbose_name="Dirección", )
    description = models.TextField(default="")
    technician = models.ForeignKey(WorkerProfile, verbose_name="Técnico", on_delete=models.PROTECT)
    date = models.DateField(verbose_name="Fecha para servicio", )

    def __str__(self):
        return str(self.client)

    def client_contact_person(self):
        return self.client.f_name + " " + self.client.l_name 

    def client_employe(self):
        return self.client.employe

    def client_phone(self):
        return self.client.phone
    
    def client_status(self):
        return self.client.state
    
    def technician_name(self):
        return self.technician.f_name + " " + self.technician.l_name

    class Meta:
        verbose_name = 'Asignacion orden de trabajo'
        verbose_name_plural = 'Asignaciones orden de trabajo'
