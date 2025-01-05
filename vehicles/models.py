from django.db import models


# Create your models here.
class Vehicle(models.Model):
    STATE_CHOICES = (('D', 'Disponible'), ('R', 'Reparación'), ('O', 'Otro'))
    id = models.AutoField(primary_key=True)
    license_plate = models.CharField('Placa vehiculo', max_length=15, null=True, blank=True)
    capacity = models.DecimalField('Capacidad vehiculo', max_digits=6, decimal_places=2, default=0)
    maintenance_date = models.DateField('Fecha mantenimiento', null=True, blank=True)
    state = models.CharField('Estado vehiculo', max_length=1, choices=STATE_CHOICES, default='D')
    observation = models.CharField('Observacion', max_length=500, null=True, blank=True)
    driver = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    model = models.ForeignKey('Model', on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.license_plate

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField('Descripcion', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Model(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField('Descripcion', max_length=100, null=True, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
