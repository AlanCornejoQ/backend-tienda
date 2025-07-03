import os
import sys
import django

# Configuracion para usar Django fuera de manage.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tienda_backend.settings")
django.setup()

from productos.factory import ProductoFactory, TipoProducto
from inventario.gestor import GestorInventario
from ordenes.comandos import OrdenCompra, EjecutarOrden

# Crear un producto y agregarlo al inventario
producto = ProductoFactory.crear_producto(
    tipo=TipoProducto.LIBRO,
    nombre="Python Pro",
    precio=100.00,
    autor="Alan Cornejo"
)

inventario = GestorInventario.get_instancia()
inventario.agregar_producto(producto, cantidad=10)

# Ejecutar una orden
orden = OrdenCompra(producto, cantidad=3)
comando = EjecutarOrden(orden)

resultado = comando.ejecutar()
print(resultado)

# Verificar nuevo stock
nuevo_stock = inventario.stock[producto.get_nombre()]["cantidad"]
print(f"Stock restante de {producto.get_nombre()}: {nuevo_stock}")
