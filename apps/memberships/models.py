from django.db import models
from teams.models import Team
from players.models import Player

class Membership(models.Model):
    joined_at = models.DateField('Data de entrada')
    is_captain = models.BooleanField('Capitão', default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Time')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Jogador')
    
    class Meta:
        verbose_name = 'Participação'
        verbose_name_plural = 'Participações'
        ordering =['id']
 
    def __str__(self):
        return f'{self.player} - {self.team}'
