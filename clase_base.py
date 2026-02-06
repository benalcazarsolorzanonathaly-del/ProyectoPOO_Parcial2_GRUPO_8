#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

from abc import ABC, abstractmethod


class ServicioGym(ABC):
    """Superclase abstracta para servicios del gimnasio."""

    def __init__(self, nombre: str, precio_base: float):
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser un string no vacío.")
        self._nombre = valor

    @property
    def precio_base(self) -> float:
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El precio base no puede ser negativo.")
        self._precio_base = valor

    @abstractmethod
    def calcular_costo(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.nombre} - ${self.precio_base:.2f}"