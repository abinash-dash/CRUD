from django.contrib import admin
from .models import Employee


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'emp_id',
        'emp_name',
        'age',
        'gender',
        'marital_status',
        'department',
        'position',
        'employment_status',
        'manager_name',
        'performance_score',
        'absences',
        'salary'
    ]

