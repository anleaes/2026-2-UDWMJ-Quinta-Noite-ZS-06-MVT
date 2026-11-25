from django.db import models
from persons.models import Person

class Player(Person):
    nickname = models.CharField('Nickname', max_length=30)
    role = models.CharField('Função', max_length=3, choices=[
        ('TOP', 'Top'),
        ('JNG', 'Jungle'),
        ('MID', 'Mid'),
        ('ADC', 'Atirador'),
        ('SUP', 'Suporte'),
    ])
    is_starter = models.BooleanField('Titular', default=True)
    photo = models.ImageField('Foto', upload_to='players')
    
    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
        ordering =['id']
 
    def __str__(self):
        return f'{self.nickname}'