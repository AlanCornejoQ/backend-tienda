from django.db import models



# Clase base para productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

    def mostrar_detalle(self) -> str:
        raise NotImplementedError("Subclases deben implementar mostrar_detalle()")

# Subclase concreta: Libro
class Libro(Producto):
    autor = models.CharField(max_length=100)

    def mostrar_detalle(self) -> str:
        return f"Libro: {self.nombre} por {self.autor} - Precio: ${self.precio}"
