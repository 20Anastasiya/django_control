from django.urls import path

from my_control.views import ListEmployee, DetailEmployee, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

app_name = 'my_control'

urlpatterns = [
    path('employees/', ListEmployee.as_view(), name='employee-list'),
    path('employee/<int:pk>', DetailEmployee.as_view(), name='employee-detail'),
    path('employee/create/', EmployeeCreateView.as_view()),
    path('employee/update/<int:pk>', EmployeeUpdateView.as_view()),
    path('employee/delete/<int:pk>', EmployeeDeleteView.as_view())
]
