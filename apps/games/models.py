from django.db import models
from matches.models import Match
from teams.models import Team

class Game(models.Model):
    game_number = models.IntegerField('Número do jogo', default=1)
    duration_minutes = models.IntegerField('Duração (minutos)', default=0)
    replay_file = models.FileField('Replay', upload_to='replays', blank=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='games', verbose_name='Partida')
    blue_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='games_blue', verbose_name='Time lado azul')
    red_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='games_red', verbose_name='Time lado vermelho')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='games_won', null=True, blank=True, verbose_name='Vencedor')
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering =['id']
 
    def __str__(self):
        return f'Jogo {self.game_number} - {self.match}'
