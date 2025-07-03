from inventario.gestor import GestorInventario
from notificaciones.observer import SujetoObservable
# Base del patron Command
class OrdenCommand:
    def ejecutar(self):
        raise NotImplementedError("Debes implementar ejecutar()")

# Receptor: representa una orden concreta
class OrdenCompra:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def procesar(self):
        inventario = GestorInventario.get_instancia()
        nombre = self.producto.get_nombre()

        stock = inventario.stock.get(nombre, {}).get("cantidad", 0)

        if stock >= self.cantidad:
            inventario.stock[nombre]["cantidad"] -= self.cantidad
            return f"Orden procesada: {self.cantidad} x {nombre}"
        else:
            return f"No hay stock suficiente para {nombre} (stock disponible: {stock})"

# Comando concreto que ejecuta la orden y notifica
class EjecutarOrden(OrdenCommand):
    def __init__(self, orden, sujeto_observable: SujetoObservable = None):
        self.orden = orden
        self.observable = sujeto_observable

    def ejecutar(self):
        resultado = self.orden.procesar()
        if self.observable:
            self.observable.notificar(resultado)
        return resultado