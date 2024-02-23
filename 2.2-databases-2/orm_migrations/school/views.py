from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):

    students = Student.objects.prefetch_related('teachers')
    students = students.order_by('group')

    template = 'school/students_list.html'
    context = {'object_list': students}

    return render(request, template, context)

# class StudentsListView(ListView):
#     model = Student
#     template_name = 'school/students_list.html'
#     context_object_name = 'object_list'
