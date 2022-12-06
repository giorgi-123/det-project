from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from . import serializers
from . import models


class DepartmentViewset(viewsets.ModelViewSet):
    queryset = models.Department.objects
    serializer_class = serializers.DepartmentSerializer
    def list(self, request):
        return Response(self.serializer_class(self.queryset.all(), many=True).data)
    
    def retrieve(self, request, pk=None):
        queryset = models.Employee.objects.filter(department=pk)
        serializer = serializers.EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployeesViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects
    serializer_class = serializers.EmployeeSerializer
    def retrieve(self, request, pk=None):
        queryset = models.Task.objects.filter(employee=pk)
        serializer = serializers.TaskSerializer(queryset, many=True)
        return Response(serializer.data)



class TasksViewset(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


