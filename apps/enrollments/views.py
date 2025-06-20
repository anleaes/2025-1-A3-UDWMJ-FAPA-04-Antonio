from django.shortcuts import render, get_object_or_404, redirect
from .forms import EnrollmentForm
from .models import Enrollment

# Create your views here.

def add_enrollment(request):
    template_name = 'enrollments/add_enrollment.html'
    context = {}
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            f = form.save(commit = False)
            f.save()
            form.save_m2m()
            return redirect('enrollments:list_enrollments')
    form = EnrollmentForm()
    context['form'] = form
    return render(request, template_name, context)

def list_enrollments(request):
    template_name = 'enrollments/list_enrollments.html'
    enrollments = Enrollment.objects.filter()
    context = {
        'enrollments': enrollments
    }
    return render(request, template_name, context)

def edit_enrollment(request, id_enrollment):
    template_name = 'enrollments/add_enrollment.html'
    context = {}
    enrollment = get_object_or_404(Enrollment, id = id_enrollment)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance = enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollments:list_enrollments')
    form = EnrollmentForm(instance = enrollment)
    context['form'] = form
    return render(request, template_name, context)

def delete_enrollment(request, id_enrollment):
    enrollment = Enrollment.objects.get(id = id_enrollment)
    enrollment.delete()
    return redirect('enrollments:list_enrollments')