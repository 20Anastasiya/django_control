from django.shortcuts import render
from django.views.generic import ListView, DetailView
from my_control.models import Employee


class ListStudent(ListView):
    model = Employee
    queryset = Employee.objects.all()


class DetailEmployee(DetailView):
    model = Employee
    queryset = Employee.objects.all()
