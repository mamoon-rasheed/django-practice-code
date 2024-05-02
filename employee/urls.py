from django.urls import path

from employee.views import adddepartment, adddesignation, addemployee

urlpatterns = [
    path('addemployee', addemployee,name='addemployee'),
    path('adddepartment', adddepartment,name='adddepartment'),
    path('adddesignation', adddesignation,name='adddesignation')
]