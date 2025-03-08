from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=255)
    
    class Meta:
        db_table = 'productos'  # <-- Aquí le dices a Django que use la tabla "productos"
        managed = False  # <-- Esto evita que Django intente crear/modificar la tabla