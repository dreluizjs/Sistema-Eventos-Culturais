from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import FuncionarioForm
from .models import Funcionario
from django.contrib import messages
from django.urls import reverse_lazy

#Função que lista todos os funcionários cadastrados
@login_required
def funcionario_list(request):
    template_name='funcionario/funcionario_list.html'
    object = Funcionario.objects.all()
    context = {'object_list': object}
    return render(request, template_name, context)

#Função que cadastra novos funcionários
@login_required
def funcionario_create(request):
    template_name='funcionario/funcionario_create.html'

    if request.method == "POST":
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionario Cadastrado com sucesso!')
            return redirect('/funcionarios/')
    else:
        form = FuncionarioForm()
    return render(request, template_name, {'form':form})

#Função que exibe informações dos funcionários de acordo com o seu ID
@login_required
def funcionario_detalhe(request, pk):
    template_name='funcionario/funcionario_detalhe.html'
    obj= Funcionario.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

#Função que deleta funcionário
@login_required
def funcionario_delete(request, pk):
    funcionario = get_object_or_404 (Funcionario, pk=pk)
    funcionario.delete()
    messages.info(request, 'Funcionario deletado com sucesso!')
    return redirect('/funcionarios/')