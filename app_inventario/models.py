from django.db import models

# Create your models here.
class Empresa(models.Model):
    nit= models.CharField(max_length=10, primary_key=True)
    nomEmpresa= models.CharField(max_length=45)
    direccion= models.CharField(max_length=45)

class Categoria(models.Model):
    idCategoria= models.PositiveSmallIntegerField(default=10)
    nomCategoria= models.CharField(max_length=45)

class Articulo(models.Model):
    idArticulo= models.PositiveSmallIntegerField(default=10)
    nomArticulo= models.CharField(max_length=45)
    cantidad= models.PositiveSmallIntegerField(default=10)
    idCategoria= models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)

class Empleado(models.Model):
    documento= models.PositiveSmallIntegerField(primary_key=True, default=5)
    nomEmpleado= models.CharField(max_length=45)
    apellidos= models.CharField(max_length=45)
    telefono= models.PositiveSmallIntegerField(default=5)
    e_mail= models.CharField(max_length=45)
    idEmpresa= models.ForeignKey(Empresa, null=False, blank=False,default=5,on_delete=models.CASCADE)

class articulo_has_empleado(models.Model):
    documento= models.PositiveSmallIntegerField(Empleado, null=False, blank=False, default=5)
    idArticulo= models.PositiveSmallIntegerField(Articulo, null=False, blank=False, default=5)