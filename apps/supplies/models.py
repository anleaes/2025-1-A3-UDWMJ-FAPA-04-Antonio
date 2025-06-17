from django.db import models

# Create your models here.

class Supply(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    quantity = models.IntegerField
    category = models.TextField('Categoria', max_length=100) 
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
        ordering =['id']

    def __str__(self):
        return self.name
