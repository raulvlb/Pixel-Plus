from mailbox import NotEmptyError
from django.db import models

# Create your models here.

class portfolio(models.Model):
    clientes = models.CharField(max_length=4)
    projetos = models.CharField(max_length=4)
    premios = models.CharField(max_length=4)

class quemsomos(models.Model):
    image = models.ImageField(upload_to='fotos')
    paragrafo = models.TextField()

class servicos1(models.Model):
    titulo = models.CharField(max_length=250)
    paragrafo = models.TextField()

class servicos2(models.Model):
    titulo = models.CharField(max_length=250)
    paragrafo = models.TextField()

class trabalhos(models.Model):
    image = models.ImageField(upload_to='fotos')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class depoimentos(models.Model):
    image = models.ImageField(upload_to='fotos')
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    depoimento = models.TextField()

class FormContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    comentario = models.TextField()

class RedesSociais(models.Model):
    facebook = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    