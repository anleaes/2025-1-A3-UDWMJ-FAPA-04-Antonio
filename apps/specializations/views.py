from django.shortcuts import render, get_object_or_404, redirect
from .forms import SpecializationForm
from .models import Specialization


# Create your views here.

def add_specialization(request):
    template_name = 'specializations/add_specialization.html'
    context = {}
    if request.method == 'POST':
        form = SpecializationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('specializations:list_specializations')
    form = SpecializationForm()
    context['form'] = form
    return render(request, template_name, context)

def list_specializations(request):
    template_name = 'specializations/list_specializations.html'
    specialization = Specialization.objects.filter()
    context = {
        'specializations': specialization
    }
    return render(request, template_name, context)

def edit_specialization(request, id_specialization):
    template_name = 'specializations/add_specialization.html'
    context = {}
    specialization = get_object_or_404(Specialization, id = id_specialization)
    if request.method == 'POST':
        form = SpecializationForm(request.POST, instance = specialization)
        if form.is_valid():
            form.save()
            return redirect('specializations:list_specializations')
    form = SpecializationForm(instance = specialization)
    context['form'] = form
    return render(request, template_name, context)

def delete_specialization(request, id_specialization):
    specialization = Specialization.objects.get(id = id_specialization)
    specialization.delete()
    return redirect('specializations:list_specializations')