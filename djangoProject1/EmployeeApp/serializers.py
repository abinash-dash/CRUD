# from abc import ABC

from rest_framework import serializers
from .models import Employee


def age_validator(age):
    if age > 60:
        raise serializers.ValidationError('Age must be "<=60 and >=0"')


def gender_validator(gender):
    if gender not in (genders := ["M", "F", "T"]):
        raise serializers.ValidationError(f'Gender must be one out of {genders}')


class EmployeeSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(validators=[age_validator,])
    gender = serializers.CharField(validators=[gender_validator,])

    class Meta:
        model = Employee
        fields = "__all__"

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.emp_id = validated_data.get('id', instance.emp_id)
        instance.emp_name = validated_data.get('name', instance.emp_name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.position = validated_data.get('position', instance.position)
        instance.employment_status = validated_data.get('employment_status', instance.employment_status)
        instance.manager_name = validated_data.get('manager_name', instance.manager_name)
        instance.performance_score = validated_data.get('performance_score', instance.performance_score)
        instance.absences = validated_data.get('absences', instance.absences)
        instance.department = validated_data.get('department', instance.department)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()
        return instance()

