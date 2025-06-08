from django.db import models
from especializacao.models import Especializacao

# Create your models here.

class Professor(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    name = models.CharField('Nome', max_length = 50)
    last_name = models.CharField('Sobrenome', max_length = 100)
    date_birth = models.DateField('Data de Nascimento', auto_now = False, auto_now_add = False) 
    GENDER_CHOICES = (
        ('H', 'Homem'),
        ('M', 'Mulher'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length = 1, choices = GENDER_CHOICES)
    address = models.CharField('Endereco', max_length = 200)
    email = models.EmailField('E-mail', null = False, blank = False)
    cellphone = models.CharField('Numero de Celular', max_length = 10)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['id']

    def __str__(self):
        return self.name
    
class EspecializacaoProfessor(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    especializacao = models.ForeignKey(Especializacao, on_delete=models.CASCADE)

class Meta:
    verbose_name = 'Especializacao do Professor'
    verbose_name_plural = 'Especializacoes do Professor'
    ordering =['id']

def __str__(self):
    return self.especializacao.name