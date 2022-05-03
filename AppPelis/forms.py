from django import forms


class PeliculaFormulario(forms.Form):

    titulo = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    duracion = forms.IntegerField()

