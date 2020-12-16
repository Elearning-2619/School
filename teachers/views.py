from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
from .models import Teacher
from .forms import TeacherCreationForm

def teachers_list_view(request):
    teachers = Teacher.objects.all()
    form = TeacherCreationForm()

    if request.is_ajax and request.method =='POST':
        form = TeacherCreationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance,])
            return JsonResponse({'instance': ser_instance, 'teacherid': instance.id}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)

    return render(request, 'teachers/list.html', {'teachers_list': teachers, 'form': form})

def teachers_detail_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teachers/detail.html', {'teacher': teacher})

def teachers_delete_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    return redirect('teachers:teachers_list')

def teachers_update_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    form = TeacherCreationForm(request.POST or None, request.FILES or None, instance=teacher)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('teachers:teachers_list')
    return render(request, 'teachers/update.html', {'form': form})