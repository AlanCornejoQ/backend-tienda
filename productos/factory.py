from .models import Libro
from enum import Enum

# Tipos posibles de producto
class TipoProducto(Enum):
    LIBRO = "libro"

# Factory Method
class ProductoFactory:
    @staticmethod
    def crear_producto(tipo: TipoProducto, **kwargs):
        if tipo == TipoProducto.LIBRO:
            return Libro.objects.create(
                nombre=kwargs.get("nombre", "Sin nombre"),
                precio=kwargs.get("precio", 0.0),
                autor=kwargs.get("autor", "Desconocido")
            )
        raise ValueError("Tipo de producto no soportado")
