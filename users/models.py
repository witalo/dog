import os

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ROL_CHOICES = (('A', 'Administrador'), ('P', 'Paseador'), ('D', 'Adiestrador'))
    document = models.CharField('Numero documento', max_length=8, null=True, blank=True)
    phone = models.CharField('Celular', max_length=9, null=True, blank=True)
    contract_date = models.DateField('Fecha contrato', null=True, blank=True)
    role = models.CharField('Rol usuario', max_length=1, choices=ROL_CHOICES, default='P')
    photo = models.ImageField('Foto', upload_to='users/', blank=True, null=True)
    address = models.CharField('Direccion', max_length=250, null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'document', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        try:
            # Obtén el usuario actual antes de guardarlo
            old_user = User.objects.get(pk=self.pk)
            if old_user.photo and old_user.photo != self.photo:
                # Si existe una foto anterior y es diferente a la nueva, elimínala
                if os.path.isfile(old_user.photo.path):
                    os.remove(old_user.photo.path)
        except User.DoesNotExist:
            # Si el usuario no existe, no hagas nada
            pass
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']

    def __str__(self):
        return self.email
