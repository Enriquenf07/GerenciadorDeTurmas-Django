from django.db import models

# Create your models here.


class Professor(models.model):
    nome = models.CharField(max_length=30)
    senha = models
