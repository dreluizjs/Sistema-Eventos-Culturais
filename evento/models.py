from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

class Evento(models.Model):

    nome            = models.CharField(max_length=50, null=True, blank=True)
    slug            = models.SlugField(max_length=100, unique=True, blank=True)
    organizador     = models.CharField(max_length=30)    
    descricao       = models.TextField(null=True, blank=True)
    #banner          = models.ImageField(upload_to = 'evento/', null=True, blank=True)
    orcamento       = models.DecimalField(max_digits=8, decimal_places=2)
    data            = models.DateField(null=True, blank=True)
    hora            = models.TimeField(null=True, blank=True)
    datainscricao   = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)
    status          = models.BooleanField(default=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Evento, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('evento:evento_detail', kwargs={'pk':self.pk})

    #def get_absolute_url(self):
     #   return "/evento/{slug}".format(slug=self.slug)