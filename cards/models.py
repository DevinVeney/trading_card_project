from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# I will only use the base rarity since the card images I have prepared match the base rarity
class Card(models.Model):
    RARITY_CHOICES = [
        ("common", "Common"),
    ]
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    image = models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.name
