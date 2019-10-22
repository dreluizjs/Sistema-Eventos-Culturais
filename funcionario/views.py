from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Funcionario
from .forms import FuncionarioForm

def funcionario_list(request):
    template_name='funcionario/funcionario_list.html'
    object= Funcionario.objects.all()
    context = {'object_list': object}
    return render(request, template_name, context)

def funcionario_create(request):
    template_name='funcionario/funcionario_create.html'

    if request.method == "POST":
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FuncionarioForm()
    return render(request, template_name, {'form':form})

def funcionario_detail(request, pk):
    template_name='funcionario/funcionario_detail.html'
    obj= Funcionario.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

def funcionario_edit(request, pk, cls):
    template_name='funcionario/funcionario_edit.html'
    obj = get_object_or_404(Funcionario, pk=pk)


    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = cls(instance=obj)

        return render(request, template_name, {'form': form})

def funcionario_delete(request, pk):
    obj = get_object_or_404(Funcionario, pk=pk)
    obj.delete()
    return redirect('/')

class FuncionarioList(ListView):
    queryset = Funcionario.objects.all()
    template_name = 'funcionario/funcionario_list.html'

class FuncionarioCreate(CreateView):
    model = Funcionario
    template_name = 'funcionario/funcionario_create.html'
    form_class = FuncionarioForm

class FuncionarioDetail(DetailView):
    model = Funcionario
    template_name = 'funcionario/funcionario_detail.html'

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    template_name = 'funcionario/funcionario_edit.html'
    form_class = FuncionarioForm

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'funcionario/funcionario_delete.html'
    success_message = 'Success: Book was deleted.'
    success_url = ('funcionarios/')