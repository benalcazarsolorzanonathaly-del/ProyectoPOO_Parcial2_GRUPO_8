#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

from dominio.clase_base import ServicioGym


class MembresiaVirtual(ServicioGym):
    """Membresía virtual del gimnasio."""

    def __init__(self, nombre: str, precio_base: float, plan_videos: str, incluye_app: bool):
        super().__init__(nombre, precio_base)
        self._plan_videos = plan_videos
        self._incluye_app = incluye_app

    @property
    def plan_videos(self) -> str:
        return self._plan_videos

    @plan_videos.setter
    def plan_videos(self, valor: str) -> None:
        if not valor or not isinstance(valor, str):
            raise ValueError("Plan de videos inválido.")
        self._plan_videos = valor

    @property
    def incluye_app(self) -> bool:
        return self._incluye_app

    @incluye_app.setter
    def incluye_app(self, valor: bool) -> None:
        self._incluye_app = valor

    def calcular_costo(self) -> float:
        costo = self.precio_base
        if self.incluye_app:
            costo += 10.00
        return costo

    def __str__(self) -> str:
        return f"{super().__str__()} - Virtual - Plan: {self.plan_videos} - App: {'Sí' if self.incluye_app else 'No'}"
