from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

class UsuarioForm(UserCreationForm):
    #email = forms.EmailField(max_length=60, help_text='Required')
    #email = forms.EmailField()
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = Usuario
        fields = ['email', 'username', 'password1', 'password2']