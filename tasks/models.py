from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    
    prioridades = [('Baja', 'De 4 a 5 días'), ('Intermedio', 'De 2 a 3 días'), ('Alta', 'De 12hrs a 1 día')]
    
    envia = models.CharField(max_length=50)
    recibe = models.CharField(max_length=50)
    fecha = models.DateTimeField(datetime.today())
    descripcion = models.CharField(max_length=100)
    prioridad = models.CharField(max_length=20, choices=prioridades)
    
    def __str__(self) -> str:
        usuarios = 'Tarea asignada de ' + self.envia + ' para ' + self.recibe
        return usuarios