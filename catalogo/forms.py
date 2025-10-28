from django import forms
from .models import Quadrinho

class QuadrinhoForm(forms.ModelForm):
    class Meta:
        model = Quadrinho
        fields = ['titulo', 'numero', 'editora', 'autor', 'data_lancamento', 'descricao']
        widgets = {
            'data_lancamento': forms.DateInput(attrs={'type': 'date'}),
        }