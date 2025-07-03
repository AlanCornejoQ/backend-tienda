import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tienda_backend.settings")
django.setup()

from productos.factory import ProductoFactory, TipoProducto
from inventario.gestor import GestorInventario
from reportes.generador import GeneradorReportes

# Setup producto y stock
libro = ProductoFactory.crear_producto(
    tipo=TipoProducto.LIBRO,
    nombre="Arquitectura de Software",
    precio=55.0,
    autor="Alan"
)

inventario = GestorInventario.get_instancia()
inventario.agregar_producto(libro, cantidad=10)

# Generar reporte
generador = GeneradorReportes()
salida = generador.generar_reporte_csv_inventario()
print(salida)
