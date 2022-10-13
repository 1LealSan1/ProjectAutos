from django.db import models


class Marcas(models.Model):
    marca = models.CharField(max_length=300, verbose_name='Marca')

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.marca
