from django.db import models
from persons.models import Person
from teams.models import Team

class Coach(Person):
    coach_role = models.CharField('Função',max_length=4, choices=[
        ('HEAD', 'Head Coach'),
        ('ASST', 'Assistente'),
        ('ANL', 'Analista'),
    ])
    nickname = models.CharField('Nickname', max_length=30)
    salary = models.DecimalField('Salário', max_digits=10, decimal_places=2, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='coaches', verbose_name='Time')

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.nickname}'