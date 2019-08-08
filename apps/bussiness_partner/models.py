from django.db import models

class Zone(models.Model):
    code = models.CharField(max_length=6, verbose_name="Código")
    description = models.CharField(max_length=50, verbose_name="Descripción zona")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

class Address(models.Model):
    address = models.CharField(max_length=200, verbose_name="Dirección")
    zone = models.ForeignKey(Zone, verbose_name="Zona", on_delete=models.PROTECT)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'

class BussinessPartner(models.Model):

    code = models.CharField(max_length=12, verbose_name="Código", primary_key=True)
    f_name = models.CharField(max_length=50, verbose_name="Primer Nombre")
    s_name = models.CharField(max_length=50, verbose_name="Segundo Nombre")
    l_name = models.CharField(max_length=50, verbose_name="Primer Apellido")
    ll_name = models.CharField(max_length=50, verbose_name="Segundo Apellido")
    employe = models.CharField(max_length=200, verbose_name="Empresa")
    address = models.ManyToManyField(Address, verbose_name="Dirección")
    phone = models.CharField(max_length=15, verbose_name="Teléfono / Cel")
    state = models.BooleanField(verbose_name="Estado", )

    def __str__(self):
        return self.code + " - " + self.f_name + " " + self.l_name
    class Meta:
        verbose_name = 'Socio de negocio'
        verbose_name_plural = 'Socios de negocio'