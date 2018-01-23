from django import forms
from .models import Devoir


class DevoirForm(forms.ModelForm):
    class Meta:
        model = Devoir
        #Les paths doivent etre rentrés automatiquements avec le nom du devoir et le dossier de la classe
        #id classe et id prof doit être remplit avec les variables
        fields = ['titre','consignes','dateDebut','dateFin','pathCorrection','pathEntrees','idProfesseur','idClasse',]




class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

