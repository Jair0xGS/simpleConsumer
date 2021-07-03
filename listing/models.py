from django.db import models

# Create your models here.
class Zona(models.Model):
    zona= models.CharField(max_length=2,primary_key=True)
    descripcion= models.CharField(max_length=50)
    ciudad= models.CharField(max_length=30)
    class Meta:
        db_table="zona"

class Cliente(models.Model):
    idCliente= models.IntegerField(primary_key=True)
    cliente= models.CharField(max_length=4)
    zona= models.ForeignKey('Zona', on_delete=models.CASCADE,db_column='zona')
    ruc= models.CharField(max_length=11)
    nombre= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    saldo= models.FloatField()
    credito= models.BooleanField()
    topeCredito= models.FloatField()
    tipoCliente= models.CharField(max_length=1)
    calificacion= models.CharField(max_length=1)
    idRepresentante= models.IntegerField()
    genero= models.BooleanField()
    class Meta:
        db_table="cliente"