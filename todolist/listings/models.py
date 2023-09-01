from django.db import models

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
    