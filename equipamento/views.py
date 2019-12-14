from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import EquipamentoForm
from .models import Equipamento
from django.contrib import messages
from django.views.generic import View, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.utils import timezone
from siseventos.render import Render


# Create your views here.


@login_required
def equipamento_create(request):
    template_name='equipamento/equipamento_create.html'

    if request.method == "POST":
        form = EquipamentoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento Cadastrado com sucesso!')
            return redirect('/equipamentos/')
    else:
        form = EquipamentoForm()
    return render(request, template_name, {'form':form})

@login_required
def equipamento_delete(request, pk):
    equipamento = get_object_or_404 (Equipamento, pk=pk)
    equipamento.delete()
    messages.info(request, 'Equipamento deletado com sucesso!')
    return redirect('/equipamentos/')


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

class Relatorio(View):

    def get(self, request):
        equipamento = Equipamento.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'equipamento': equipamento,
            'request': request
        }
        return Render.render('equipamento/equipamento_report.html', params)