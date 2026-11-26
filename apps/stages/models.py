from django.db import models
from tournaments.models import Tournament

class Stage(models.Model):
    name = models.CharField('Nome', max_length=50)
    stage_type = models.CharField('Tipo', max_length=3, choices=[
        ('GRP', 'Fase de grupos'),
        ('KO', 'Mata-mata'),
        ('FIN', 'Final'),
    ])
    order = models.IntegerField('Ordem', default=1)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, verbose_name='Torneio')
    
    class Meta:
        verbose_name = 'Fase'
        verbose_name_plural = 'Fases'
        ordering =['id']
 
    def __str__(self):
        return f'{self.name}'
