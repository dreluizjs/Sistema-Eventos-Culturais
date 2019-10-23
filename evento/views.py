from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EventoForm
from .models import Evento
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


@login_required
def lista_evento(request):
    template_name='evento/evento_list.html'
    object= Evento.objects.all()
    context = {'object_list': object}
    return render(request, template_name, context)

@login_required
def cadastro_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            #login(request, account)
            messages.success(request,f'Conta criada para {username}!')            
            return redirect('/evento/')
    else:
        form = EventoForm()
    return render (request, 'evento/evento_registro.html', {'form':form})


@login_required
def delete_evento(request, pk):
    evento = get_object_or_404 (Evento, pk=pk)
    evento.delete()

    messages.info(request, 'Evento deletado com sucesso!')

    return redirect('/evento/')



class EventoList(ListView):
    queryset = Evento.objects.all()
    template_name = 'evento/evento_list.html'

class EventoCreate(CreateView):
    model = Evento
    template_name = 'evento/evento_create.html'
    form_class = EventoForm

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
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('evento/')



