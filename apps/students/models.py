from django.db import models

# Create your models here.

class Student(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    birth_year = models.DateField('Ano de Nascimento', max_length=4)
    gender = models.CharField('Genero', max_length=1, choices=(('H', 'Homem'),('M', 'Mulher'),('O', 'Outro')))
    address = models.CharField('Endereço', max_length=200)   
    cell_phone = models.CharField('Telefone', max_length=12)
    email = models.EmailField('E-mail',null=False, blank=False)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['id']

    def __str__(self):
        return self.first_name