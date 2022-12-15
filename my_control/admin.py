from django.contrib import admin

from my_control.models import Department, Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fio', 'position', 'salary', 'department')
    list_filter = ('fio', 'salary')
    search_fields = ('fio', 'position')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
