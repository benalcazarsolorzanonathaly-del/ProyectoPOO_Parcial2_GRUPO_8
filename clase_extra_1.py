#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra


class Cliente:
    """Clase para clientes del gimnasio."""

    def __init__(self, id_cliente: int, nombre: str, telefono: str):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._telefono = telefono

    @property
    def id_cliente(self) -> int:
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("ID no puede ser negativo.")
        self._id_cliente = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor:
            raise ValueError("Nombre no puede estar vacío.")
        self._nombre = valor

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        if not valor:
            raise ValueError("Teléfono no puede estar vacío.")
        self._telefono = valor

    def __str__(self) -> str:
        return f"Cliente {self.id_cliente}: {self.nombre}"
