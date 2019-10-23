from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EventoForm
from .models import Evento, Despesa
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


@login_required
def evento_list(request):
    template_name='evento/evento_list.html'
    object= Evento.objects.all()
    context = {'object_list': object}
    return render(request, template_name, context)

@login_required
def evento_delete(request, pk):
    evento = get_object_or_404 (Evento, pk=pk)
    evento.delete()
    messages.info(request, 'Evento deletado com sucesso!')
    return redirect('/evento/')

@login_required
def despesa_evento(request, evento_slug):
    evento = get_object_or_404(Evento, slug=evento_slug)
    template_name ='despesa/evento_despesa.html'
    context = {'evento': evento, 'despesa_list': evento.despesas.all()}
    return render(request, template_name, context)

class EventoList(ListView):
    queryset = Evento.objects.all()
    template_name = 'evento/evento_list.html'

class EventoCreate(CreateView):
    model = Evento
    template_name = 'evento/evento_create.html'
    form_class = EventoForm
    success_message = 'Evento cadastrado com sucesso.'

class EventoDetail(DetailView):
    model = Evento
    template_name = 'evento/evento_detail.html'

class EventoUpdate(UpdateView):
    model = Evento
    template_name = 'evento/evento_edit.html'
    form_class = EventoForm

class EventoDelete(DeleteView):
    model = Evento
    template_name = 'evento/evento_delete.html'
    success_message = 'Evento foi deletado.'
    success_url = reverse_lazy('evento/')

class DespesaList(ListView):
    queryset = Despesa.objects.all()
    template_name = 'despesa/despesa_list.html'




