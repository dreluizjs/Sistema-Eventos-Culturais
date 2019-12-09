from django import forms
from django.forms import ModelForm
from .models import Evento, Despesa
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Reset, Row, Column


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'organizador','descricao','orcamento','data','hora','status','banner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='form-group col-md-6 mb-0'),
                Column('organizador', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('orcamento', css_class='form-group col-md-4 mb-0'),
                Column('data', css_class='form-group col-md-4 mb-0'),
                Column('hora', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
             Row(
                Column('status', css_class='form-group col-md-4 mb-0'),
                Column('banner', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
             Row(
                Column('descricao', css_class='form-group col-md-8 mb-0'),
            ),
            Submit('submit', 'Cadastrar'),
            Reset('reset', 'Limpar')
        )
        
class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields =  '__all__'

class DespesaForm2(forms.Form):
    titulo = forms.CharField()
    montante = forms. DecimalField()
    descricao = forms.CharField()

