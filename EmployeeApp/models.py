from django.db import models


# 1.	Define a model for an employee that contains the following fields: id, name, age, gender, department, salary.
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    marital_status = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    employment_status = models.CharField(max_length=30)
    manager_name = models.CharField(max_length=50)
    performance_score = models.CharField(max_length=30)
    absences = models.IntegerField()
    salary = models.FloatField()