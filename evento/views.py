from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EventoForm, DespesaForm
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
def evento_create(request):
    template_name='evento/evento_create.html'

    if request.method == "POST":
        form = EventoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Evento Cadastrado com sucesso!')
            return redirect('/eventos/')
    else:
        form = EventoForm()
    return render(request, template_name, {'form':form})

@login_required
def evento_delete(request, pk):
    evento = get_object_or_404 (Evento, pk=pk)
    evento.delete()
    messages.info(request, 'Evento deletado com sucesso!')
    return redirect('/eventos/')

class EventoDetail(DetailView):
    model = Evento
    template_name = 'evento/evento_detail.html'


@login_required
def despesa_evento(request, pk):
    evento = get_object_or_404 (Evento, pk=pk)
    template_name ='despesa/evento_despesa.html'
    context = {'evento': evento, 'despesa_list': evento.despesas.all()}
    return render(request, template_name, context)

@login_required
def despesa_create(request):
    template_name='despesa/despesa_create.html'

    if request.method == "POST":
        form = DespesaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/eventos/despesa')
    else:
        form = DespesaForm()
    return render(request, template_name, {'form':form})

class DespesaList(ListView):
    queryset = Despesa.objects.all()
    template_name = 'despesa/despesa_list.html'

class DespesaCreate(CreateView):
    model = Despesa
    template_name = 'despesa/despesa_create.html'
    form_class = Despesa
    success_message = 'Despesa cadastrada com sucesso.'




