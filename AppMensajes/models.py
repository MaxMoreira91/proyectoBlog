from django.db import models

class Emisor(models.Model):
    nombre= models.CharField(max_length=30)
    

class Receptor(models.Model):
    nombre= models.CharField(max_length=30)

class Mensaje(models.Model):
    texto= models.TextField()

