from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone

SEXO = [
    ("F", "Feminino"),
    ("M", "Masculino"),
    ("N", "Nenhuma das opções")
]

class Funcionario(models.Model):

    nome       = models.CharField(max_length=50)
    slug       = models.SlugField(max_length=100, unique=True, blank=True)
    rg         = models.CharField(max_length=32)
    cpf        = models.CharField(max_length=32)
    sexo       = models.CharField(max_length=1, choices=SEXO, blank=False, null=False)
    cpf        = models.CharField(max_length=32)
    nascimento = models.DateField(null=True, blank=True)
    email      = models.EmailField(max_length=50)
    telefone   = models.CharField(max_length=50)
    cargo      = models.CharField(max_length=50, null=True, blank=True)   
    #endereco   = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True, blank=True)
    criado     = models.DateTimeField(auto_now_add=True)
    update     = models.DateTimeField(auto_now=True)
    ativo      = models.BooleanField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Funcionario, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('funcionario:funcionario_detail', kwargs={'pk':self.pk})