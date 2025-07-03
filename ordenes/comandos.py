class OrdenCommand:
    def ejecutar(self):
        raise NotImplementedError("Debes implementar ejecutar()")


# Receptor: la orden real que se ejecuta
class OrdenCompra:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def procesar(self):
        return f"Orden procesada: {self.cantidad} x {self.producto.nombre}"
    

# Comando concreto
class EjecutarOrden(OrdenCommand):
    def __init__(self, orden):
        self.orden = orden

    def ejecutar(self):
        return self.orden.procesar()
