from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClassForm
from .models import Class

# Create your views here.

def add_class(request):
    template_name = 'classes/add_class.html'
    context = {}
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('classes:list_classes')
    form = ClassForm()
    context['form'] = form
    return render(request, template_name, context)

def list_classes(request):
    template_name = 'classes/list_classes.html'
    classes = Class.objects.filter()
    context = {
        'classes': classes
    }
    return render(request, template_name, context)

def edit_class(request, id_class):
    template_name = 'classes/add_class.html'
    context = {}
    classes = get_object_or_404(Class, id = id_class)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance = classes)
        if form.is_valid():
            form.save()
            return redirect('classes:list_classes')
    form = ClassForm(instance = classes)
    context['form'] = form
    return render(request, template_name, context)

def delete_class(request, id_class):
    classes = Class.objects.get(id = id_class)
    classes.delete()
    return redirect('classes:list_classes')