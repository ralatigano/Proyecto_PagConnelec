from django.shortcuts import render
from .models import Project

# Create your views here.
def vistaProyectos(request):
    proyectos=Project.objects.all()
    return render(request, 'portfolio/portafolio.html', {"portafolio":proyectos})