from django.shortcuts import render, get_object_or_404, redirect

from .forms import EspecializacaoForm
from .models import Especializacao

# Create your views here.

def add_especializacao(request):
    template_name = 'especializacao/add_especializacao.html'
    context = {}
    if request.method == 'POST':
        form = EspecializacaoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('especializacao:list_especializacoes')
    form = EspecializacaoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_especializacoes(request):
    template_name = 'especializacao/list_especializacoes.html'
    especializacoes = Especializacao.objects.filter()
    context = {
        'especializacoes': especializacoes
    }
    return render(request, template_name, context)

def edit_especializacao(request, id_especializacao):
    template_name = 'especializacao/add_especializacao.html'
    context ={}
    especializacao = get_object_or_404(Especializacao, id=id_especializacao)
    if request.method == 'POST':
        form = EspecializacaoForm(request.POST, instance=especializacao)
        if form.is_valid():
            form.save()
            return redirect('especializacao:list_especializacoes')
    form = EspecializacaoForm(instance=especializacao)
    context['form'] = form
    return render(request, template_name, context)

def delete_especializacao(request, id_especializacao):
    especializacao = Especializacao.objects.get(id=id_especializacao)
    especializacao.delete()
    return redirect('especializacao:list_especializacoes')