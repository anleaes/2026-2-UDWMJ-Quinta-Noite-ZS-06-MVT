from django.db import models
from games.models import Game
from champions.models import Champion

class Draft(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='draft', verbose_name='Jogo')
    blue_picks = models.ManyToManyField(Champion, related_name='drafts_blue_picks', verbose_name='Picks lado azul')
    red_picks = models.ManyToManyField(Champion, related_name='drafts_red_picks', verbose_name='Picks lado vermelho')
    blue_bans = models.ManyToManyField(Champion, related_name='drafts_blue_bans', blank=True, verbose_name='Bans lado azul')
    red_bans = models.ManyToManyField(Champion, related_name='drafts_red_bans', blank=True, verbose_name='Bans lado vermelho')
    
    class Meta:
        verbose_name = 'Draft'
        verbose_name_plural = 'Drafts'
        ordering =['id']
 
    def __str__(self):
        return f'Draft - {self.game}'
