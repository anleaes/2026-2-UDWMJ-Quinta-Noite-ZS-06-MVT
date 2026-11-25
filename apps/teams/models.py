from django.db import models

class Team(models.Model):
    name = models.CharField('Nome', max_length=50)
    tag = models.CharField('Sigla', max_length=10)
    created_at = models.DateField('Data de criação')
    logo = models.ImageField('Logo', upload_to='teams')
    
    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'
        ordering = ['id']

    def __str__(self):
        return self.name