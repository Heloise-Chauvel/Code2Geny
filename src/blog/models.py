from django.db import models

# Create your models here.
class classe(models.Model):
    nom=models.CharField(max_length=100)
    professeur=models.CharField(max_length=100)

class devoir(models.Model):
    idDevoir=models.CharField(max_length=100)
    titre=models.CharField(max_length=100)
    dateDebut=models.DateField
    dateFin=models.DateField
    pathSujet=models.CharField(max_length=100)
    pathCorrection=models.CharField(max_length=100)
    pathEntrees=models.CharField(max_length=100)
    idProfesseur=models.CharField(max_length=100)

class realisation(models.Model):
       note=models.IntegerField
       idEtudiant=models.CharField(max_length=100)
       emailEtudiant=models.CharField(max_length=100)
       idDevoir=models.CharField(max_length=100)


