from django.db import models

class Integrante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return self.nombre+ ""+str(self.apellido)

class Post(models.Model):
    titulo= models.CharField(max_length=30)
    contenido= models.TextField()
    autor= models.CharField(max_length=30)

    def __str__(self):
        return self.titulo+ ""+str(self.autor)
