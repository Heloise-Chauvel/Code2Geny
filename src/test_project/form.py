from django import forms
from .models import Devoir
from .models import Realisation

#dans cette classe se trouvent tout les form de l'application

class DevoirForm(forms.ModelForm):
    class Meta:

        #Définition du model suivi
        model = Devoir

        #Selection des champs a afficher
        fields = ['titre','consignes','dateDebut','dateFin','pathCorrection','pathEntrees','idProfesseur','idClasse',]

class rendreDevoirForm(forms.ModelForm):
    class Meta:

        #Définition du model suivi
        model = Realisation

        #Selection des champs a afficher
        fields = ['reponse','idEtudiant','emailEtudiant','idDevoir']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

