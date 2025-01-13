# Generated by Django 5.1.4 on 2025-01-12 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.CharField(blank=True, max_length=8, null=True, verbose_name='Numero documento')),
                ('names', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre completo')),
                ('phone', models.CharField(blank=True, max_length=9, null=True, verbose_name='Celular')),
                ('email', models.EmailField(blank=True, max_length=150, null=True, verbose_name='Correo')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Direccion')),
                ('contact', models.CharField(choices=[('C', 'Correo'), ('W', 'WhatsApp'), ('F', 'Facebook'), ('L', 'LLamada'), ('O', 'Otros')], default='L', max_length=1, verbose_name='Metodo contacto')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_state', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
