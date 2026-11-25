from django.db import models

class Person(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100)
    birth_date = models.DateField('Data de Nascimento')
    phone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('Email', blank=False, null=False)
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'