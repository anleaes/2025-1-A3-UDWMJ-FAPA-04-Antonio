from django.db import models
from supplies.models import Supply

# Create your models here.

class Room(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    number = models.IntegerField('Numero')
    capacity = models.IntegerField('Capacidade')
    supplies = models.ForeignKey(Supply, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['id']

    def __str__(self):
        return self.name