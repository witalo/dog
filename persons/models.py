from django.db import models


# Create your models here.
class Person(models.Model):
    CONTACT_CHOICES = (('C', 'Correo'), ('W', 'WhatsApp'), ('F', 'Facebook'), ('L', 'LLamada'), ('O', 'Otros'))
    id = models.AutoField(primary_key=True)
    document = models.CharField('Numero documento', max_length=8, null=True, blank=True)
    names = models.CharField('Nombre completo', max_length=250, null=True, blank=True)
    phone = models.CharField('Celular', max_length=9, null=True, blank=True)
    email = models.EmailField('Correo', max_length=150, null=True, blank=True)
    address = models.CharField('Direccion', max_length=250, null=True, blank=True)
    contact = models.CharField('Metodo contacto', max_length=1, choices=CONTACT_CHOICES, default='L')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_state = models.BooleanField(default=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
