class Observador:
    def actualizar(self, mensaje):
        raise NotImplementedError("Debes implementar actualizar()")


# Observador concreto
class NotificadorEmail(Observador):
    def actualizar(self, mensaje):
        print(f"[Email] Enviando notificacion: {mensaje}")


# Sujeto observable
class SujetoObservable:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar(self, mensaje):
        for obs in self.observadores:
            obs.actualizar(mensaje)
