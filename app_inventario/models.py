from django.db import models

# Create your models here.
class Empresa(models.Model):
    nit= models.CharField(max_length=10, primary_key=True, verbose_name='nit')
    nomEmpresa= models.CharField(max_length=45)
    direccion= models.CharField(max_length=45)


    def __str__(self) -> str:
        return f"{self.nomEmpresa} ({self.direccion})";

class Categoria(models.Model):
    idCategoria= models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', editable=False)
    nomCategoria= models.CharField(max_length=45)

    def __str__(self) -> str:
        return f"{self.nomCategoria}"

class Articulo(models.Model):
    idArticulo= models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', editable=False)
    nomArticulo= models.CharField(max_length=45)
    cantidad= models.PositiveSmallIntegerField(default=10)
    idCategoria= models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nomArticulo} Cantidad: {self.cantidad}"

class Empleado(models.Model):
    documento= models.CharField(primary_key=True, null=False, verbose_name='documento', max_length=45)
    nomEmpleado= models.CharField(max_length=45)
    apellidos= models.CharField(max_length=45)
    telefono= models.IntegerField()
    e_mail= models.CharField(max_length=45)
    idEmpresa= models.ForeignKey(Empresa, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('documento','idEmpresa'));

    def __str__(self) -> str:
        return f"{self.nomEmpleado} {self.apellidos} ({self.documento}) Perteneciente a: {self.idEmpresa.nomEmpresa}"

class articulo_has_empleado(models.Model):
    documento= models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
    idArticulo= models.ForeignKey(Articulo, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.documento.nomEmpleado}: Articulo {self.idArticulo.nomArticulo}."
    
    def dashboard(self):
        dataset = {}
        dataset['registros'] = self.objects.all()
        dataset['total_assigned'] = len(dataset['registros']);
        total_articles = sum(list(Articulo.objects.all()),'cantidad',0);
        return dataset
