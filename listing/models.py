from django.db import models
from django.db import connection
# Create your models here.
class Zona(models.Model):
    zona= models.CharField(max_length=2,primary_key=True)
    descripcion= models.CharField(max_length=50)
    ciudad= models.CharField(max_length=30)
    class Meta:
        db_table="zona"
    def __str__(self):
        return self.descripcion + " - "+ self.ciudad

class Cliente(models.Model):
    idCliente= models.IntegerField()
    cliente= models.CharField(max_length=4,primary_key=True)
    zona= models.ForeignKey('Zona', on_delete=models.CASCADE,db_column='zona')
    ruc= models.CharField(max_length=11,default='00000000001')
    nombre= models.CharField(max_length=50,default='')
    direccion= models.CharField(max_length=50,default='')
    saldo= models.FloatField(default=0.0)
    credito= models.BooleanField(default=False)
    topeCredito= models.FloatField(default=0.0)
    tipoCliente= models.CharField(max_length=1,default='A')
    calificacion= models.CharField(max_length=1,default='A')
    idRepresentante= models.IntegerField(default=1)
    genero= models.CharField(default='M',max_length=1)
    class Meta:
        db_table="cliente"
    def save(self,*args,**kwargs):
        self._meta.local_fields=[f for f in self._meta.local_fields if f.name not in ('idCliente')]
        cursor=connection.cursor()
        query= """EXEC _RegistrarCliente 
        @nombre = '{nombre}', 
        @tipo = {tipo},
        @id='{id}',
        @zona='{zona}',
        @ruc='{ruc}',
        @Direccion='{direccion}',
        @credito='{credito}',
        @tipocli='{tipocli}'
        """.format(
            nombre=self.nombre,
            tipo =1,
            tipocli=self.tipoCliente,
            id=self.cliente,
            zona=self.zona.zona,
            ruc=self.ruc,
            direccion=self.direccion,
            credito=self.credito,
        )
        cursor.execute(query)