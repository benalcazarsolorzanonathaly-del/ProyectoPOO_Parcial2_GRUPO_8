#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

from typing import List
from dominio.clase_base import ServicioGym


class GestorGym:
    """Gestor de servicios del gimnasio."""

    def __init__(self):
        self._servicios = []

    def agregar_servicio(self, servicio: ServicioGym) -> None:
        self._servicios.append(servicio)

    def calcular_total_ingresos(self, servicios: List[ServicioGym]) -> float:
        total = 0.0
        for servicio in servicios:
            total += servicio.calcular_costo()
        return total

    def generar_reporte(self, servicios: List[ServicioGym]) -> str:
        reporte = ["=== REPORTE DE SERVICIOS ==="]
        for servicio in servicios:
            reporte.append(str(servicio))
        reporte.append(f"Total servicios: {len(servicios)}")
        return "\n".join(reporte)

    def __str__(self) -> str:
        return f"Gestor con {len(self._servicios)} servicios"
