from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.

def add_student(request):
    template_name = 'students/add_student.html'
    context = {}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('students:list_students')
    form = StudentForm()
    context['form'] = form
    return render(request, template_name, context)

def list_students(request):
    template_name = 'students/list_students.html'
    students = Student.objects.filter()
    context = {
        'students': students
    }
    return render(request, template_name, context)

def edit_student(request, id_student):
    template_name = 'students/add_student.html'
    context = {}
    student = get_object_or_404(Student, id = id_student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return redirect('students:list_students')
    form = StudentForm(instance = student)
    context['form'] = form
    return render(request, template_name, context)

def delete_student(request, id_student):
    student = Student.objects.get(id = id_student)
    student.delete()
    return redirect('students:list_students')