from django.db import models

class Dog(models.Model):
    nome = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    nascimento = models.DateField( auto_now=False, auto_now_add=False)
    email = models.EmailField()
