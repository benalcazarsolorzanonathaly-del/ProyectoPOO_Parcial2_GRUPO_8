#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

import sys
import pyodbc as bd


class DatabaseConnection:


    # ========== CONFIGURAR ESTOS VALORES ==========
    _SERVIDOR = 'DESKTOP-OMLK3LH\\SQLKERSEYLOOR'  # TU SERVIDOR
    _BBDD = 'GimnasioDB'  # NOMBRE DE TU BASE
    _USUARIO = 'admin_gimnasio'  # TU USUARIO SQL
    _PASSWORD = '1234'  # TU CONTRASEÑA
    # ==============================================

    _conexion = None
    _cursor = None

    @classmethod
    def obtener_conexion(cls):
        """
        Obtiene la conexión a la BBDD con los parámetros de conexión pasados como constantes.
        """
        if cls._conexion is None:
            try:
                connection_string = (
                    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                    f"SERVER={cls._SERVIDOR};"
                    f"DATABASE={cls._BBDD};"
                    f"UID={cls._USUARIO};"
                    f"PWD={cls._PASSWORD};"
                    f"TrustServerCertificate=yes"  # ← IMPORTANTE
                )

                cls._conexion = bd.connect(connection_string)
                print(f"✅ Conexión exitosa a: {cls._SERVIDOR}")
                return cls._conexion

            except Exception as e:
                print(f"❌ Error de conexión: {e}")
                print("\n⚠️  SOLUCIÓN DE PROBLEMAS:")
                print(f"1. Servidor: {cls._SERVIDOR}")
                print(f"2. Base de datos: {cls._BBDD}")
                print(f"3. Usuario: {cls._USUARIO}")
                print("4. Verifica que 'GimnasioDB' exista (ejecuta db.sql)")
                print("5. Verifica que SQL Server esté ejecutándose")
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtener_cursor(cls):
        """
        Obtiene el cursor para ejecutar consultas.
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtener_conexion().cursor()
                print("✅ Cursor obtenido correctamente")
                return cls._cursor
            except Exception as e:
                print(f"❌ Error al obtener cursor: {e}")
                sys.exit()
        else:
            return cls._cursor

    @classmethod
    def ejecutar_consulta(cls, consulta: str, parametros: tuple = None):
        """
        Ejecuta una consulta SQL.
        """
        cursor = cls.obtener_cursor()
        try:
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)

            if consulta.strip().upper().startswith('SELECT'):
                return cursor.fetchall()
            else:
                cls._conexion.commit()
                return cursor.rowcount

        except Exception as e:
            cls._conexion.rollback()
            print(f"❌ Error en consulta: {e}")
            raise

    @classmethod
    def cerrar_conexion(cls):
        """
        Cierra la conexión y el cursor.
        """
        if cls._cursor:
            cls._cursor.close()
            cls._cursor = None
        if cls._conexion:
            cls._conexion.close()
            cls._conexion = None
        print("🔌 Conexión cerrada")


# Prueba de conexión al ejecutar directamente
if __name__ == '__main__':
    print("=" * 60)
    print("PRUEBA DE CONEXIÓN CON CONFIGURACIÓN DEL PROFESOR")
    print("=" * 60)

    try:
        conexion = DatabaseConnection.obtener_conexion()
        cursor = DatabaseConnection.obtener_cursor()

        # Probar consulta
        cursor.execute("SELECT @@VERSION AS version")
        version = cursor.fetchone()[0]

        print(f"\n✅ ✅ CONEXIÓN EXITOSA!")
        print(f"📡 Servidor: {DatabaseConnection._SERVIDOR}")
        print(f"📁 Base de datos: {DatabaseConnection._BBDD}")
        print(f"👤 Usuario: {DatabaseConnection._USUARIO}")
        print(f"🔧 Versión SQL Server: {version[:80]}...")

        # Verificar si existe la tabla Membresias
        cursor.execute("""
            SELECT TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_NAME = 'Membresias'
        """)

        if cursor.fetchone():
            print("✅ Tabla 'Membresias' encontrada")
        else:
            print("⚠️  Tabla 'Membresias' NO encontrada. Ejecuta db.sql")

        DatabaseConnection.cerrar_conexion()

    except Exception as e:
        print(f"\n❌ PRUEBA FALLIDA: {e}")

    input("\nPresiona Enter para salir...")