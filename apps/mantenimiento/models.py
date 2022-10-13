from django.db import models

from apps.autos.models import Autos


class Mantenimientos(models.Model):
    kilometraje = models.PositiveIntegerField(verbose_name='Kilometraje')
    descripcion = models.CharField(max_length=7, verbose_name='Descripcion')
    costo = models.PositiveIntegerField(verbose_name='Costo')
    fecha = models.DateTimeField(verbose_name='Fecha')
    auto = models.ForeignKey(Autos, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return ' %s %s %s %s %s' % (self.auto, self.fecha, self.costo, self.descripcion, self.kilometraje)
