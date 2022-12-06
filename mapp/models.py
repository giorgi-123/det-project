from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.department_name
    
    class Meta:
        ordering = ['id']

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name + " " + self.surname

    class Meta:
        ordering = ['id']

class Task(models.Model):
    task = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.task



