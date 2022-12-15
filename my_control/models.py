from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name='Название отдела', max_length=50)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=50)
    position = models.CharField(verbose_name='Должность', max_length=50)
    salary = models.FloatField(verbose_name='Зарплата', )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.fio}{self.position}{self.salary}{self.department}'
