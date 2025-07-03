from abc import ABC, abstractmethod

# Componente base
class ReporteBase(ABC):
    @abstractmethod
    def generar(self):
        pass

# Componente concreto
class ReporteInventario(ReporteBase):
    def __init__(self, datos):
        self.datos = datos

    def generar(self):
        lineas = [f"{p.nombre} - Stock: {cantidad}" for p, cantidad in self.datos]
        return "\n".join(lineas)

# Decorador base
class ReporteDecorator(ReporteBase):
    def __init__(self, componente: ReporteBase):
        self.componente = componente

    def generar(self):
        return self.componente.generar()

# Decorador concreto: CSV
class ReporteCSVDecorator(ReporteDecorator):
    def generar(self):
        salida_original = self.componente.generar()
        lineas = salida_original.split("\n")
        csv_lineas = ["producto,stock"]
        for linea in lineas:
            partes = linea.split(" - Stock: ")
            if len(partes) == 2:
                csv_lineas.append(f"{partes[0]},{partes[1]}")
        return "\n".join(csv_lineas)
