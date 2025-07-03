import os
import sys
import django

# Configuracion para usar Django sin manage.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tienda_backend.settings")
django.setup()

from productos.factory import ProductoFactory, TipoProducto
from inventario.gestor import GestorInventario
from ordenes.comandos import OrdenCompra, EjecutarOrden
from notificaciones.observer import NotificadorEmail, SujetoObservable

# Crear producto
producto = ProductoFactory.crear_producto(
    tipo=TipoProducto.LIBRO,
    nombre="Django 101",
    precio=60.0,
    autor="Alan C."
)

# Agregar al inventario
inventario = GestorInventario.get_instancia()
inventario.agregar_producto(producto, cantidad=3)

# Crear observador y sujeto
notificador = NotificadorEmail()
observable = SujetoObservable()
observable.agregar_observador(notificador)

# Crear y ejecutar orden
orden = OrdenCompra(producto, cantidad=2)
comando = EjecutarOrden(orden, sujeto_observable=observable)
resultado = comando.ejecutar()

# Ver resultado
print("Resultado:", resultado)
