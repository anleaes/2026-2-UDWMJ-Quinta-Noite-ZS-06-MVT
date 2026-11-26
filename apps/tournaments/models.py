from django.db import models

class Tournament(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=500)
    start_date = models.DateField('Data de Início')
    end_date = models.DateField('Data de Término')
    prize = models.DecimalField('Premiação', max_digits=12, decimal_places=2, default=0)
    status = models.CharField('Situação', max_length=3, default='OPN', choices=[
        ('OPN', 'Inscrições Abertas'),
        ('RUN', 'Em Andamento'),
        ('END', 'Encerrado'),
        ])
    rules_doc = models.FileField('Regulamento', upload_to='docs')
    
    class Meta:
        verbose_name = 'Torneio'
        verbose_name_plural = 'Torneios'
        ordering = ['id']
    
    def __str__(self):
        return self.name