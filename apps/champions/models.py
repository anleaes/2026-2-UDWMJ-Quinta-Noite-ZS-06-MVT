from django.db import models

class Champion(models.Model):
    name = models.CharField(max_length=100)
    pick_rate = models.FloatField('Pick rate (%)', null=True, blank=True, default=0.0)
    ban_rate = models.FloatField('Ban rate (%)', null=True, blank=True, default=0.0)
    icon = models.ImageField('Icone', upload_to='champions')

    class Meta:
        verbose_name = 'Campeão'
        verbose_name_plural = 'Campeões'
        ordering = ['id']

    def __str__(self):
        return self.name

