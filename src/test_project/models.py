from django.db import models
from django.urls import reverse
from django.utils import timezone

from django import forms
import datetime
from . import settings
# Create your models here.
class Classe(models.Model):
    nom=models.CharField(max_length=100)
    professeur=models.CharField(max_length=100)

    def __str__(self):
        return self.nom + ' - '+ self.professeur

class Devoir(models.Model):
    idDevoir=models.CharField(max_length=100)
    titre=models.CharField(max_length=100)
    dateDebut=models.CharField(max_length=100,default=timezone.now)
    dateFin= models.CharField(max_length=10, default='00/00/0000')
    pathSujet=models.CharField(max_length=100)
    pathCorrection=models.FileField(max_length=100)
    pathEntrees=models.FileField(max_length=100)
    consignes=models.TextField(default='')
    idProfesseur=models.CharField(max_length=100)
    idClasse=models.CharField(max_length=100,  default='')

    def __str__(self):
        return ' ID ' + self.idDevoir + ' - TITRE  '+ self.titre + ' - PROF  '+ self.idProfesseur + ' -ID CLASSE '+ self.idClasse

class Realisation(models.Model):
       note=models.IntegerField(default='0')
       idEtudiant=models.CharField(max_length=100)
       emailEtudiant=models.EmailField(max_length=100)
       idDevoir=models.CharField(max_length=100)
       reponse=models.FileField(default='')

class Participe(models.Model):
    idEtudiant=models.CharField(max_length=100,default='')
    idDevoir=models.CharField(max_length=100,default='')
    def __str__(self):
        return ' IDETUDIANT ' + self.idEtudiant + ' - IDDEVOIR  '+ self.idDevoir


class Appartient(models.Model):
    idEtudiant=models.CharField(max_length=100,default='')
    idClasse=models.CharField(max_length=100,default='')
