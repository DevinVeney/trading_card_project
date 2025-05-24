from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        
    ]
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    image = models.ImageField(upload_to='cards/')
    description = models.TextField()

    def __str__(self):
        return self.name

class UserCollection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Collection"
