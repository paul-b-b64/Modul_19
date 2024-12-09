from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=80)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=80)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    size = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)
