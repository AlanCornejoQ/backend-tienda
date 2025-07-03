class GestorInventario:
    _instancia = None

    def __init__(self):
        if GestorInventario._instancia is not None:
            raise Exception("Ya existe una instancia. Usar get_instancia()")
        self.productos = []

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        return self.productos

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]
