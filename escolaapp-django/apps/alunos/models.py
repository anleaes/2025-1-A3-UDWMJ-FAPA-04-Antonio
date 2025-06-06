from django.db import models

# Create your models here.

class Aluno(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    name = models.CharField('Nome', max_length = 50)
    date_birth = models.DateField('Data de Nascimento', auto_now = False, auto_now_add = False) 
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length = 1, choices = GENDER_CHOICES)
    email = models.EmailField('E-mail', null = False, blank = False)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering =['id']

    def __str__(self):
        return self.name
