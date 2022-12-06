from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Depratments', views.DepartmentViewset, basename='Departments')
router.register(r'Employees', views.EmployeesViewset, basename='Employees')
router.register(r'Add-Tasks', views.TasksViewset, basename='Tasks')


urlpatterns = [
    path('', include(router.urls)),
    path('sapi/', include('rest_framework.urls')),

]
