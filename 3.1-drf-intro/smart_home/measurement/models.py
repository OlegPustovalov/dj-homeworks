from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание') 

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor =  models.ForeignKey(Sensor, on_delete=models.CASCADE,related_name='measurements')
    temperature = models.IntegerField()
    created_at = models.DateTimeField(verbose_name='Дата измерения')
    
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

