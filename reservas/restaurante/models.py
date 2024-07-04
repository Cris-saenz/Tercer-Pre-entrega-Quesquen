from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=14)

    def __str__(self):
        return self.nombre
    
class Mesa(models.Model):
    numero = models.CharField(max_length=10)
    capacidad = models.PositiveIntegerField(max_length=30)
    def __str__(self):
        return self.numero
    
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField()
    motivo_especial = models.CharField(max_length=100)
    def __str__(self):
        return f"¡La reserva se acompletado con exito! para el {self.fecha_reserva}, N° de mesas {self.mesa.numero} a Nombre de {self.cliente.nombre}"