from django import forms
from django.forms import ModelForm
from .models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields =  '__all__'
