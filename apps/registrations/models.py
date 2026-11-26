from django.db import models
from teams.models import Team
from tournaments.models import Tournament

class Registration(models.Model):
    registered_at = models.DateTimeField('Data da inscrição', auto_now_add=True)
    status = models.CharField('Situação', max_length=4, default='PEND', choices=[
        ('PEND', 'Pendente'),
        ('CONF', 'Confirmada'),
        ('REFU', 'Recusada'),
    ])
    fee = models.DecimalField('Taxa', max_digits=10, decimal_places=2, default=0)
    payment_proof = models.FileField('Comprovante', upload_to='proofs')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Time')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, verbose_name='Torneio')
    
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering =['id']
 
    def __str__(self):
        return f'{self.team} - {self.tournament}'
