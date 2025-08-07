from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from employee.models import Employee

# Create your views here.
def employee_detial(request , pk):
    employee = get_object_or_404(Employee, pk=pk)
    return HttpResponse(employee)