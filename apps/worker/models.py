from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Gender(models.Model):
    id = models.AutoField(primary_key=True)
    prefix = models.CharField(max_length=1)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"

class Dependence(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Dependencia"
        verbose_name = "Dependencias"

class Position(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=150)
    dependence = models.ForeignKey(Dependence, on_delete=models.PROTECT)

    def __str__(self):
        return self.description + " - " + self.dependence.description

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

class TypeId(models.Model):
    id = models.AutoField(primary_key=True)
    prefix = models.CharField(max_length=10)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Tipo de identificación"
        verbose_name_plural = "Tipos de identificación"

class WorkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    f_name = models.CharField(max_length=50, blank=True, null=True)
    s_name = models.CharField(max_length=50, blank=True, null=True)
    l_name = models.CharField(max_length=50, blank=True, null=True)
    ll_name = models.CharField(max_length=50, blank=True, null=True)
    born_date = models.DateField(blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT, blank=True, null=True)
    type_id = models.ForeignKey(TypeId, on_delete=models.PROTECT, blank=True, null=True)
    id_number = models.CharField(max_length=15, blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        try:
            return self.f_name + " " + self.s_name + " " + self.l_name + " " + self.ll_name
        except TypeError:
            return self.user.username + " (definir pefil)"

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        print(instance)
        WorkerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.workerprofile.save()
