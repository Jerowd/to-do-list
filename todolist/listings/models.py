from django.db import models
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    jour = models.fields.DateField()
    class Importance(models.TextChoices):
        FAIBLE = 'Faible',
        MOYENNE = 'Moyenne',
        ELEVEE = 'Elevée'
    titre = models.fields.TextField(max_length=100)
    description = models.fields.TextField(max_length=2000)
    finie = models.fields.BooleanField(default = False)

    def __str__(self) -> str:
        return f'{self.titre}'
    
    def get_absolute_url(self):
        return reverse('update_task', args=[str(self.id)])  # Utilisé pour obtenir l'URL de mise à jour de la tâche
    