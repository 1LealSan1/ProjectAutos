from django.db import models

from apps.marca.models import Marcas


class Modelos(models.Model):
    modelo = models.CharField(max_length=300, verbose_name='Modelo')
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return '%s %s' % (self.modelo, self.marca)
