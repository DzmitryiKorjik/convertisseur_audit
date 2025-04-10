from django import forms

class UploadFileForm(forms.Form):
    fichier = forms.FileField(label="Choisir un fichier .txt ou .csv")