from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
import datetime

# Create your views here.
def home(request):
    tareas = Task.objects.all()
    return render(request, 'home.html', {'tareas': tareas})

def form_add(request):
    return render(request, 'form_add.html',{})

def agregar(request):
    envias = request.POST['envia']
    recibes = request.POST['recibe']
    descripcions = request.POST['descripcion']
    prioridads = request.POST['prioridad']

    agregar_task = Task.objects.create(
        envia=envias,
        recibe=recibes,
        fecha=datetime.date.today(),
        descripcion=descripcions,
        prioridad=prioridads)
    
    return redirect('/')

def form_edit(request, id):
    tarea = get_object_or_404(Task, pk=id)
    return render(request, 'form_edit.html',{'tarea': tarea})

def actualizar(request, id):
    envias = request.POST['envia']
    recibes = request.POST['recibe']
    descripcions = request.POST['descripcion']
    prioridads = request.POST['prioridad']
    
    tarea = Task.objects.get(id = id)
    tarea.envia=envias
    tarea.recibe=recibes
    tarea.descripcion=descripcions
    tarea.prioridad=prioridads
    
    tarea.save()
    return redirect('/')

def borrar(request, id):
    tarea = Task.objects.get(id = id)
    tarea.delete()
    
    return redirect('/')