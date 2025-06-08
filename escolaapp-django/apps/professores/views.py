from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProfessorForm
from .models import Professor, Especializacao, EspecializacaoProfessor

# Create your views here.

def add_professor(request):
    template_name = 'professores/add_professor.html'
    context = {}
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('professores:list_professores')
    form = ProfessorForm()
    context['form'] = form
    return render(request, template_name, context)

def list_professores(request):
    template_name = 'professores/list_professores.html'
    especializacaoProfessor = EspecializacaoProfessor.objects.filter()
    especializacao = Especializacao.objects.filter()
    professor = Professor.objects.filter()
    context = {
        'professor': professor,
        'especializao': especializacao,
        'especializaoProfessor': especializacaoProfessor
    }
    return render(request, template_name, context)

def edit_professor(request, id_professor):
    template_name = 'professores/add_professor.html'
    context ={}
    professor = get_object_or_404(Professor, id=id_professor)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance = professor)
        if form.is_valid():
            form.save()
            return redirect('professores:list_professores')
    form = ProfessorForm(instance = professor)
    context['form'] = form
    return render(request, template_name, context)

def delete_professor(request, id_professor):
    professor = Professor.objects.get(id = id_professor)
    professor.delete()
    return redirect('professores:list_professores')
