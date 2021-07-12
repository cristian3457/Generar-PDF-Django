from django.urls import path
from . import views
urlpatterns = [
    path('listar-empleados/',views.ListEmpleadosPdf, name='empleados_all'),
    path('empleados/',views.empleados, name='empleados')
]