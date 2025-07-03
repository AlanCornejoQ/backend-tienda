import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tienda_backend.settings")
django.setup()

from productos.factory import ProductoFactory, TipoProducto
from inventario.gestor import GestorInventario

# Crear producto
libro = ProductoFactory.crear_producto(
    tipo=TipoProducto.LIBRO,
    nombre="Imaginaria",
    precio=35.00,
    autor="Cristopher rodas"
)

# Acceder al singleton
inventario = GestorInventario.get_instancia()
inventario.agregar_producto(libro)

# Verificar
for p in inventario.listar_productos():
    print(p.mostrar_detalle())
