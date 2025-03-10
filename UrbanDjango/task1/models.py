from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.DecimalField(max_digits=7, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buers')

    def __str__(self):
        return f'{self.title} | {self.description}. Стоимость: {self.cost}'


# Create your models here.
