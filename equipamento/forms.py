from django import forms
from django.forms import ModelForm
from .models import Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields =  '__all__'
