from rest_framework import serializers

from . import models

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('id','department_name')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id','name', 'surname', 'email', 'address', 'age', 'department')
        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'task', 'employee')