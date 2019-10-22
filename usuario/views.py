from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm
from .models import Usuario
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DeleteView


@login_required
def usuario_list(request):
    template_name='usuario/usuario_list.html'
    object= Usuario.objects.all()
    context = {'object_list': object}
    return render(request, template_name, context)

@login_required
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            #login(request, account)
            messages.success(request,f'Conta criada para {username}!')            
            return redirect('/usuario/')
    else:
        form = UsuarioForm()
    return render (request, 'usuario/usuario_create.html', {'form':form})

@login_required
def usuario_detail(request, pk):
    template_name='usuario/usuario_detail.html'
    obj= Usuario.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

@login_required
def usuario_delete(request, pk):
    usuario = get_object_or_404 (Usuario, pk=pk)
    usuario.delete()

    messages.info(request, 'Usuario deletado com sucesso!')

    return redirect('/usuario/')
    
class UsuarioUpdate(UpdateView):
    model = Usuario
    template_name = 'usuario/usuario_edit.html'
    form_class = UsuarioForm
