from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

TIPO = [
    ("E", "Estrutura"),
    ("I", "Iluminação"),    
    ("S", "Som"),
    ("O", "Outro"),
]

class Equipamento(models.Model):

    nome        = models.CharField(max_length=40)
    slug        = models.SlugField(max_length=100, unique=True, blank=True)
    tipo        = models.CharField(max_length=1, choices=TIPO, blank=True, null=False)
    marca       = models.CharField(max_length=25)
    modelo      = models.CharField(max_length=25)
    dimensao    = models.CharField(max_length=25, null=True, blank=True)
    valor       = models.FloatField()
    quantidade  = models.IntegerField(null=True, blank=True)
    descricao   = models.TextField(null=True, blank=True)
    #imagem      = models.ImageField(upload_to = 'equipamento/', null=True, blank=True)
    criado      = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)
    ativo       = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Equipamento, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse_lazy('equipamento:equipamento_detail', kwargs={'pk':self.pk})
