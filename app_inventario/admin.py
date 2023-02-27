from django.contrib import admin
from app_inventario.models import *

# Register your models here.
admin.site.register(articulo_has_empleado)
admin.site.register(Empleado)
admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Empresa)