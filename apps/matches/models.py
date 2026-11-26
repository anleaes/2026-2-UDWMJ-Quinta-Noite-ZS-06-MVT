from django.db import models
from stages.models import Stage
from teams.models import Team

class Match(models.Model):
    scheduled_at = models.DateTimeField('Data e hora')
    best_of = models.IntegerField('Formato', default=3, choices=[
        (1, 'Melhor de 1'),
        (3, 'Melhor de 3'),
        (5, 'Melhor de 5'),
    ])
    status = models.CharField('Situação', max_length=3, default='SCH', choices=[
        ('SCH', 'Agendada'),
        ('RUN', 'Em andamento'),
        ('FIN', 'Finalizada'),
    ])
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name='Fase')
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_team_a', verbose_name='Time A')
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_team_b', verbose_name='Time B')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_won', null=True, blank=True, verbose_name='Vencedor')
    
    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'
        ordering =['id']
 
    def __str__(self):
        return f'{self.team_a} x {self.team_b}'

