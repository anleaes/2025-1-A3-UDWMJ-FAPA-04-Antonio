from django.db import models
from students.models import Student
from classes.models import Class

# Create your models here.

class Enrollment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date_start = models.DateField('Data de Início')
    STATUS_CHOICES = (
        ('Ativa', 'Ativa'),
        ('Finalizada', 'Finalizada'),
        ('Cancelada', 'Cancelada'),
    )
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=20, null=True, blank=False, default='Ativa')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classesEnrollment = models.ManyToManyField(Class)
    
    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        ordering =['id']

    def __str__(self):
        return self.date_start