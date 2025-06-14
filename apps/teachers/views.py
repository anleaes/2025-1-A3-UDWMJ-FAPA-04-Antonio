from django.shortcuts import render, get_object_or_404, redirect
from .forms import TeacherForm
from .models import Teacher

# Create your views here.

def add_teacher(request):
    template_name = 'teachers/add_teacher.html'
    context = {}
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('teachers:list_teachers')
    form = TeacherForm()
    context['form'] = form
    return render(request, template_name, context)

def list_teachers(request):
    template_name = 'teachers/list_teachers.html'
    teachers = Teacher.objects.filter()
    context = {
        'teachers': teachers
    }
    return render(request, template_name, context)

def edit_teacher(request, id_teacher):
    template_name = 'teachers/add_teacher.html'
    context = {}
    teacher = get_object_or_404(Teacher, id = id_teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance = teacher)
        if form.is_valid():
            form.save()
            return redirect('students:list_students')
    form = TeacherForm(instance = teacher)
    context['form'] = form
    return render(request, template_name, context)

def delete_teacher(request, id_teacher):
    teacher = Teacher.objects.get(id = id_teacher)
    teacher.delete()
    return redirect('teachers:list_teachers')