import io

from .pagination import MyPagination
from rest_framework.parsers import JSONParser
from .serializers import EmployeeSerializer
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from django.core.paginator import Paginator


# 2.	Create an API endpoint that allows users to create new employees.


@csrf_exempt
def Employee_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


# 4.	Create an API endpoint that returns a single employee by ID.

@csrf_exempt
def Employee_id(request, emp_id):
    if request.method == "POST":
        try:
            emp = Employee.objects.get(emp_id=emp_id)
            serializer = EmployeeSerializer(emp)
            resp = {
                "status": 200,
                'emp_data': serializer.data
            }
        except Exception as e:
            resp = {
                'status': 800,
                'response': e.__str__()
            }
        finally:
            json_data = JSONRenderer().render(resp)
            return HttpResponse(json_data, content_type='application/json')


# 5.	Create an API endpoint that allows users to update an existing employee.
@csrf_exempt
def Employee_update(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        emp_id = python_data.get('emp_id')
        emp = Employee.objects.get(emp_id=emp_id)
        serializer = EmployeeSerializer(emp, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


# 3.	Create an API endpoint that returns a list of all employees with a pagination option.

class EmployeeListPagination(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination


# 6.	Create an API endpoint that allows users to delete an employee.
def deletion(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        emp_id = pythondata.get('emp_id')
        emp = Employee.objects.get(emp_id=emp_id)
        emp.delete()
        res = {'msg': 'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
