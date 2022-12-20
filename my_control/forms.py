from django import forms
from django.core.exceptions import ValidationError

from .models import Employee, Department


class CreateForm(forms.ModelForm):
    fio = forms.CharField(label='ФИО')
    position = forms.CharField(label='Должность', widget=forms.widgets.Textarea())
    salary = forms.CharField(label='Зарплата', required=False)
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        label='Отдел',
        widget=forms.widgets.Select(attrs={'size': 3}),
        required=False
        )

    class Meta:
        model = Employee
        fields = ('fio', 'position', 'salary', 'department')
