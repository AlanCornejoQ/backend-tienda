class GestorInventario:
    _instancia = None

    def __init__(self):
        if GestorInventario._instancia is not None:
            raise Exception("Ya existe una instancia. Usar get_instancia()")
        self.stock = {}  # Diccionario para almacenar producto + cantidad

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def agregar_producto(self, producto, cantidad=1):
        nombre = producto.get_nombre()  # Metodo que debe estar en Producto
        if nombre in self.stock:
            self.stock[nombre]["cantidad"] += cantidad
        else:
            self.stock[nombre] = {
                "producto": producto,
                "cantidad": cantidad
            }

    def listar_productos(self):
        return [
            (info["producto"], info["cantidad"])
            for info in self.stock.values()
        ]

    def buscar_por_nombre(self, nombre):
        return [
            (info["producto"], info["cantidad"])
            for clave, info in self.stock.items()
            if nombre.lower() in clave.lower()
        ]
