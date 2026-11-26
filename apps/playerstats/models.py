from django.db import models
from games.models import Game
from players.models import Player
from champions.models import Champion

class PlayerGameStat(models.Model):
    kills = models.IntegerField('Abates', default=0)
    deaths = models.IntegerField('Mortes', default=0)
    assists = models.IntegerField('Assistências', default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='stats', verbose_name='Jogo')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Jogador')
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE, verbose_name='Campeão')
    
    class Meta:
        verbose_name = 'Estatística do jogador'
        verbose_name_plural = 'Estatísticas dos jogadores'
        ordering =['id']
 
    def __str__(self):
        return f'{self.player} - {self.champion} ({self.game})'
