from django import forms
from django.forms import ModelForm
from .models import Evento, Despesa


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields =  '__all__'
        
class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields =  '__all__'

