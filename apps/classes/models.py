from django.db import models

# Create your models here.

class Class(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    course_load = models.IntegerField('Carga Horária')
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering =['id']

    def __str__(self):
        return self.name
