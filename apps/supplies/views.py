from django.shortcuts import render, get_object_or_404, redirect
from .forms import SupplyForm
from .models import Supply

# Create your views here.

def add_supply(request):
    template_name = 'categories/add_supply.html'
    context = {}
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            f.save()
            form.save_m2m()
            return redirect('supplies:list_supplies')
    form = SupplyForm()
    context['form'] = form
    return render(request, template_name, context)

def list_supplies(request):
    template_name = 'categories/list_supplies.html'
    supplies = Supply.objects.filter()
    context = {
        'supplies': supplies
    }
    return render(request, template_name, context)

def edit_supply(request, id_category):
    template_name = 'supplies/add_supply.html'
    context ={}
    supply = get_object_or_404(Supply, id = id_category)
    if request.method == 'POST':
        form = SupplyForm(request.POST, instance = supply)
        if form.is_valid():
            form.save()
            return redirect('supplies:list_supplies')
    form = SupplyForm(instance = supply)
    context['form'] = form
    return render(request, template_name, context)

def delete_supply(request, id_category):
    supply = Supply.objects.get(id=id_category)
    supply.delete()
    return redirect('supplies:list_supplies')