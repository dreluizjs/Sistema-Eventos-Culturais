from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

class Evento(models.Model):

    nome            = models.CharField(max_length=50, null=True, blank=True)
    slug            = models.SlugField(max_length=100, unique=True, blank=True)
    organizador     = models.CharField(max_length=30)    
    descricao       = models.TextField(null=True, blank=True)
    orcamento       = models.DecimalField(max_digits=8, decimal_places=2)
    data            = models.DateField(null=True, blank=True)
    hora            = models.TimeField(null=True, blank=True)
    datainscricao   = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)
    status          = models.BooleanField(default=True, null=True, blank=True)    
    banner         = models.ImageField(upload_to = 'evento/', null=True, blank=True) 
    
    def __str__(self):
        return self.nome    
            
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Evento, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('evento:evento_detail', kwargs={'pk':self.pk})

    #def get_absolute_url(self):
     #   return "/evento/{slug}".format(slug=self.slug)
          
    
    def orcamento_left(self):
        despesa_list = Despesa.objects.filter(evento=self)
        total_despesa_montante = 0
        for despesa in despesa_list:
            total_despesa_montante += despesa.montante
        
        return self.orcamento - total_despesa_montante

    def total_montante(self):
        despesa_list = Despesa.objects.filter(evento=self)
        total = 0
        for despesa in despesa_list:
            total += montante
        
        return self.total
  
    def total_transacao(self):
        despesa_list = Despesa.objects.filter(evento=self)
        return len(despesa_list)


class Despesa(models.Model):

    evento          = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='despesas')
    titulo          = models.CharField(max_length=25, null=True, blank=True)
    montante        = models.DecimalField(max_digits=8, decimal_places=2)
    descricao       = models.TextField(null=True, blank=True)
    datalancamento  = models.DateTimeField(auto_now_add=True)
