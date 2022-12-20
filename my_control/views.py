from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from my_control.forms import CreateForm
from my_control.models import Employee


class ListEmployee(ListView):
    model = Employee
    queryset = Employee.objects.all()
    template_name = 'employee/list.html'


class DetailEmployee(DetailView):
    model = Employee
    queryset = Employee.objects.all()
    template_name = 'employee/detail.html'


class EmployeeCreateView(CreateView):
    template_name = 'employee/create.html'
    form_class = CreateForm
    success_url = reverse_lazy('my_control:employee-list')


class EmployeeUpdateView(UpdateView):
    template_name = 'employee/create.html'
    form_class = CreateForm
    model = Employee
    success_url = reverse_lazy('my_control:employee-list')


class EmployeeDeleteView(DeleteView):
    template_name = 'employee/delete.html'
    model = Employee
    success_url = reverse_lazy('my_control:employee-list')
