from reportes.base import ReporteInventario, ReporteCSVDecorator
from inventario.gestor import GestorInventario

class GeneradorReportes:
    def generar_reporte_csv_inventario(self):
        inventario = GestorInventario.get_instancia()
        datos = inventario.listar_productos()
        reporte = ReporteInventario(datos)
        reporte_csv = ReporteCSVDecorator(reporte)
        return reporte_csv.generar()
