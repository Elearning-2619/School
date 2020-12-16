from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from .forms import StudentForm
def students_list_view(request):
    students = Student.objects.all()
    form = StudentForm()

    if request.method == 'POST':
    	form = StudentForm(request.POST, request.FILES)

    	if form.is_valid():
    		saving = form.save()
    		return HttpResponse('Valid')

    	else:
    		return HttpResponse('Invalid')
    return render(request, 'students/list.html', {'students_list':students, 'form':form})

def students_detail_view(request, student_slug):
    student = get_object_or_404(Student, slug = student_slug)
    return render(request, 'students/detail', {'student':student})

def students_delete_view(request, student_slug):
    student = get_object_or_404(Student, slug = student_slug)
    student.delete()
    return redirect('students:students_list')

def students_update_view(request, student_slug):
    student = get_object_or_404(Student, slug = student_slug)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('students:students_list')
    return render(request, 'students/update.html', {'form': form})
