from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EquipamentoForm
from .models import Equipamento
from django.contrib import messages
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class EquipamentoList(ListView):
    queryset = Equipamento.objects.all()
    template_name = 'equipamento/equipamento_list.html'

class EquipamentoCreate(CreateView):
    model = Equipamento
    template_name = 'equipamento/equipamento_create.html'
    form_class = EquipamentoForm

class EquipamentoDetail(DetailView):
    model = Equipamento
    template_name = 'equipamento/equipamento_detail.html'

class EquipamentoUpdate(UpdateView):
    model = Equipamento
    template_name = 'equipamento/equipamento_edit.html'
    form_class = EquipamentoForm

class EquipamentoDelete(DeleteView):
    model = Equipamento
    template_name = 'equipamento/equipamento_delete.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('equipamento/')