from django.db import models



""" Temperature """
# значение
# дата


class Temperature(models.Model):
    value = models.FloatField(verbose_name='Значение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    room = models.ForeignKey('Place', on_delete=models.PROTECT, verbose_name='Комната')

    class Meta:
        verbose_name = "Температура"
        ordering = ['-created_at']

    def __str__(self):
        return 'temperature'


class Humidity(models.Model):
    value = models.FloatField(verbose_name='Значение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    room = models.ForeignKey('Place', on_delete=models.PROTECT, verbose_name='Комната')

    class Meta:
        verbose_name = "Влажность"
        ordering = ['-created_at']

    def __str__(self):
        return 'humidity'

class Pressure(models.Model):
    value = models.FloatField(verbose_name='Значение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    room = models.ForeignKey('Place', on_delete=models.PROTECT, verbose_name='Комната')

    class Meta:
        verbose_name = "Давление"
        ordering = ['-created_at']

    def __str__(self):
        return 'pressure'


class Place(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"
        ordering = ['name']

    def __str__(self):
        return self.name
