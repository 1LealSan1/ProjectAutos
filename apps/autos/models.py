from django.db import models

from apps.modelo.models import Modelos
from apps.user.models import User


class Autos(models.Model):
    placa = models.CharField(max_length=7, verbose_name='Placa')
    kilometraje = models.PositiveIntegerField(verbose_name='Kilometraje')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelos, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return '%s %s %s' % (self.placa, self.kilometraje, self.user)
