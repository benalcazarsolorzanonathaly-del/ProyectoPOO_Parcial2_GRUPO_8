#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

from dominio.clase_base import ServicioGym


class MembresiaPresencial(ServicioGym):
    """Membresía presencial del gimnasio."""

    def __init__(self, nombre: str, precio_base: float, acceso_sala: bool, acceso_clases: bool):
        super().__init__(nombre, precio_base)
        self._acceso_sala = acceso_sala
        self._acceso_clases = acceso_clases

    @property
    def acceso_sala(self) -> bool:
        return self._acceso_sala

    @acceso_sala.setter
    def acceso_sala(self, valor: bool) -> None:
        self._acceso_sala = valor

    @property
    def acceso_clases(self) -> bool:
        return self._acceso_clases

    @acceso_clases.setter
    def acceso_clases(self, valor: bool) -> None:
        self._acceso_clases = valor

    def calcular_costo(self) -> float:
        costo = self.precio_base
        if self.acceso_sala:
            costo += 20.00
        if self.acceso_clases:
            costo += 15.00
        return costo

    def __str__(self) -> str:
        return f"{super().__str__()} - Presencial - Sala: {'Sí' if self.acceso_sala else 'No'} - Clases: {'Sí' if self.acceso_clases else 'No'}"