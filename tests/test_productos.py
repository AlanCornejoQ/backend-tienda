import os
import sys
import django

# Agregar la ruta del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tienda_backend.settings")
django.setup()

from productos.factory import ProductoFactory, TipoProducto

# Crear un libro de prueba
libro = ProductoFactory.crear_producto(
    tipo=TipoProducto.LIBRO,
    nombre="Clean Code",
    precio=99.00,
    autor="Robert C. Martin"
)

print(libro.mostrar_detalle())
