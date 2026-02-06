#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

class MembresiaService:
    """Servicio para operaciones de membresías (intermediario entre UI y DAO)."""

    def __init__(self):
        print("✅ Servicio de membresías inicializado")

    def crear_presencial(self, nombre: str, precio: float, sala: bool, clases: bool) -> dict:
        """
        CREATE: Crea una membresía presencial.
        Returns: Dict con resultado de la operación.
        """
        try:
            from datos.membresia_dao import MembresiaDAO

            datos = {
                'nombre': nombre,
                'precio_base': precio,
                'tipo': 'Presencial',
                'acceso_sala': 1 if sala else 0,
                'acceso_clases': 1 if clases else 0
            }

            id_creado = MembresiaDAO.crear(datos)
            return {
                'exito': True,
                'mensaje': f'Membresía presencial "{nombre}" creada con ID: {id_creado}',
                'id': id_creado
            }
        except Exception as e:
            return {
                'exito': False,
                'mensaje': f'Error al crear membresía: {str(e)}'
            }

    def crear_virtual(self, nombre: str, precio: float, plan: str, app: bool) -> dict:
        """
        CREATE: Crea una membresía virtual.
        """
        try:
            from datos.membresia_dao import MembresiaDAO

            datos = {
                'nombre': nombre,
                'precio_base': precio,
                'tipo': 'Virtual',
                'plan_videos': plan,
                'incluye_app': 1 if app else 0
            }

            id_creado = MembresiaDAO.crear(datos)
            return {
                'exito': True,
                'mensaje': f'Membresía virtual "{nombre}" creada con ID: {id_creado}',
                'id': id_creado
            }
        except Exception as e:
            return {
                'exito': False,
                'mensaje': f'Error al crear membresía: {str(e)}'
            }

    def buscar_por_id(self, id_membresia: int) -> dict:
        """
        READ: Busca una membresía por ID.
        """
        try:
            from datos.membresia_dao import MembresiaDAO

            resultado = MembresiaDAO.obtener_por_id(id_membresia)
            if resultado:
                return {
                    'exito': True,
                    'data': {
                        'id': resultado[0],
                        'nombre': resultado[1],
                        'precio': float(resultado[2]),
                        'tipo': resultado[3],
                        'fecha': resultado[8]
                    }
                }
            else:
                return {
                    'exito': False,
                    'mensaje': f'Membresía con ID {id_membresia} no encontrada'
                }
        except Exception as e:
            return {
                'exito': False,
                'mensaje': f'Error al buscar: {str(e)}'
            }

    def buscar_por_nombre(self, nombre: str) -> dict:
        """
        READ: Busca membresías por nombre.
        """
        try:
            from datos.membresia_dao import MembresiaDAO

            resultados = MembresiaDAO.obtener_por_nombre(nombre)
            return {
                'exito': True,
                'mensaje': f'Búsqueda completada para: {nombre}',
                'data': resultados
            }
        except Exception as e:
            return {
                'exito': False,
                'mensaje': f'Error en búsqueda: {str(e)}',
                'data': []
            }

    def obtener_todas(self) -> dict:
        """
        READ: Obtiene todas las membresías.
        """
        try:
            from datos.membresia_dao import MembresiaDAO

            resultados = MembresiaDAO.obtener_todas()
            return {
                'exito': True,
                'mensaje': f'Se encontraron {len(resultados)} membresías',
                'data': resultados
            }
        except Exception as e:
            return {
                'exito': False,
                'mensaje': f'Error al obtener membresías: {str(e)}',
                'data': []
            }

    def actualizar(self, id_membresia: int, datos: dict) -> dict:
        """
        UPDATE: Actualiza una membresía.
        """
        try:
            from datos.membresia_dao import MembresiaDAO

            exito = MembresiaDAO.actualizar(id_membresia, datos)
            if exito:
                return {
                    'exito': True,
                    'mensaje': f'Membresía {id_membresia} actualizada correctamente'
                }
            else:
                return {
                    'exito': False,
                    'mensaje': f'No se pudo actualizar la membresía {id_membresia}'
                }
        except Exception as e:
            return {
                'exito': False,
                'mensaje': f'Error al actualizar: {str(e)}'
            }

    def eliminar(self, id_membresia: int) -> dict:
        """
        DELETE: Elimina una membresía.
        """
        try:
            from datos.membresia_dao import MembresiaDAO

            exito = MembresiaDAO.eliminar(id_membresia)
            if exito:
                return {
                    'exito': True,
                    'mensaje': f'Membresía {id_membresia} eliminada correctamente'
                }
            else:
                return {
                    'exito': False,
                    'mensaje': f'No se pudo eliminar la membresía {id_membresia}'
                }
        except Exception as e:
            return {
                'exito': False,
                'mensaje': f'Error al eliminar: {str(e)}'
            }

    def obtener_estadisticas(self) -> dict:
        """
        Obtiene estadísticas del sistema.
        """
        try:
            from datos.membresia_dao import MembresiaDAO

            stats = MembresiaDAO.obtener_estadisticas()
            return {
                'exito': True,
                'data': {
                    'total': stats['total'],
                    'presencial': stats['presencial'],
                    'virtual': stats['virtual'],
                    'promedio': round(float(stats['promedio'] or 0), 2)
                }
            }
        except Exception as e:
            return {
                'exito': False,
                'mensaje': f'Error al obtener estadísticas: {str(e)}'
            }
