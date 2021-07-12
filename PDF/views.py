
from django.shortcuts import render
from django.http import HttpResponse
#
from .models import Empleado
#
from .utils import render_to_pdf
#
from django.views.generic import View
from generarPDF import settings
def empleados(request):
    empleados = Empleado.objects.all()
    return render(request,'empleados.html',{'empleados':empleados})

def ListEmpleadosPdf(request):

    logo = settings.STATIC_URL + "assets/images/logo.png"
    empleados = Empleado.objects.all()
    data = {
        'count': empleados.count(),
        'empleados': empleados,
        'logo':logo
    }
    pdf = render_to_pdf('lista.html', data)
    return HttpResponse(pdf, content_type='application/pdf')