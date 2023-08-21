from django import forms
from .models import CategoriaComputador, Localizacao, Computador, Fila, Chamada

class CategoriaComputadorForm(forms.ModelForm):
    class Meta:
        model = CategoriaComputador
        fields = ['nome', 'descricao']

class LocalizacaoForm(forms.ModelForm):
    class Meta:
        model = Localizacao
        fields = ['nome', 'endereco', 'descricao']
    

class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computador
        fields = {'hostname','nome','categoria','localizacao'}

class FilaForm(forms.ModelForm):
    class Meta:
        model = Fila
        fields = {'nome','codigo'}

class ChamadaForm(forms.ModelForm):
    class Meta:
        model = Chamada
        fields = '__all__'
