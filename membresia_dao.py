#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

from datos.conexion import DatabaseConnection


class MembresiaDAO:
    """Data Access Object para operaciones CRUD de membresías en SQL Server."""

    @staticmethod
    def crear(datos: dict) -> int:
        """
        CREATE: Inserta una nueva membresía.
        Returns: ID de la membresía creada.
        """
        consulta = """
        INSERT INTO Membresias (nombre, precio_base, tipo, acceso_sala, acceso_clases, plan_videos, incluye_app)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        SELECT SCOPE_IDENTITY();
        """
        params = (
            datos['nombre'],
            datos['precio_base'],
            datos['tipo'],
            datos.get('acceso_sala', 0),
            datos.get('acceso_clases', 0),
            datos.get('plan_videos'),
            datos.get('incluye_app', 0)
        )
        resultado = DatabaseConnection.ejecutar_consulta(consulta, params)
        return int(resultado[0][0]) if resultado else 0

    @staticmethod
    def obtener_por_id(id_membresia: int) -> tuple:
        """
        READ: Obtiene una membresía por ID.
        Returns: Tupla con datos o None si no existe.
        """
        consulta = "SELECT * FROM Membresias WHERE id_membresia = ? AND activo = 1"
        resultados = DatabaseConnection.ejecutar_consulta(consulta, (id_membresia,))
        return resultados[0] if resultados else None

    @staticmethod
    def obtener_por_nombre(nombre: str) -> list:
        """
        READ: Busca membresías por nombre (búsqueda parcial).
        Returns: Lista de tuplas con resultados.
        """
        consulta = "SELECT * FROM Membresias WHERE nombre LIKE ? AND activo = 1"
        return DatabaseConnection.ejecutar_consulta(consulta, (f'%{nombre}%',))

    @staticmethod
    def obtener_todas() -> list:
        """
        READ: Obtiene todas las membresías activas.
        Returns: Lista de todas las membresías.
        """
        consulta = "SELECT * FROM Membresias WHERE activo = 1 ORDER BY id_membresia"
        return DatabaseConnection.ejecutar_consulta(consulta)

    @staticmethod
    def actualizar(id_membresia: int, datos: dict) -> bool:
        """
        UPDATE: Actualiza una membresía existente.
        Returns: True si se actualizó, False si no.
        """
        campos = []
        valores = []
        for campo, valor in datos.items():
            campos.append(f"{campo} = ?")
            valores.append(valor)
        valores.append(id_membresia)

        consulta = f"UPDATE Membresias SET {', '.join(campos)} WHERE id_membresia = ?"
        filas = DatabaseConnection.ejecutar_consulta(consulta, tuple(valores))
        return filas > 0

    @staticmethod
    def eliminar(id_membresia: int) -> bool:
        """
        DELETE: Elimina (desactiva) una membresía (borrado lógico).
        Returns: True si se eliminó, False si no.
        """
        consulta = "UPDATE Membresias SET activo = 0 WHERE id_membresia = ?"
        filas = DatabaseConnection.ejecutar_consulta(consulta, (id_membresia,))
        return filas > 0

    @staticmethod
    def obtener_estadisticas() -> dict:
        """
        Obtiene estadísticas de las membresías.
        Returns: Diccionario con estadísticas.
        """
        consultas = {
            'total': "SELECT COUNT(*) FROM Membresias WHERE activo = 1",
            'presencial': "SELECT COUNT(*) FROM Membresias WHERE tipo = 'Presencial' AND activo = 1",
            'virtual': "SELECT COUNT(*) FROM Membresias WHERE tipo = 'Virtual' AND activo = 1",
            'promedio': "SELECT AVG(precio_base) FROM Membresias WHERE activo = 1"
        }

        stats = {}
        for nombre, consulta in consultas.items():
            resultado = DatabaseConnection.ejecutar_consulta(consulta)
            stats[nombre] = resultado[0][0] if resultado else 0

        return stats
