#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

# main_qt.py
import sys
import os
from datetime import datetime

print("=" * 90)
print("🏋️  SISTEMA DE GESTIÓN DE GIMNASIO - GRUPO 8")
print("2do PARCIAL: POO + Qt UI + CRUD con SQL Server")
print("=" * 90)

# Configurar rutas
ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ruta_proyecto)
sys.path.insert(0, os.path.join(ruta_proyecto, 'datos'))
sys.path.insert(0, os.path.join(ruta_proyecto, 'servicio'))
sys.path.insert(0, os.path.join(ruta_proyecto, 'ui_qt'))

print(f"\n📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"📁 Proyecto: {ruta_proyecto}")

# Probar conexión SQL
try:
    from datos.conexion import DatabaseConnection

    print("\n🔗 PROBANDO CONEXIÓN SQL SERVER...")
    conexion = DatabaseConnection.obtener_conexion()
    cursor = DatabaseConnection.obtener_cursor()

    cursor.execute("SELECT @@VERSION")
    version = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Membresias WHERE activo = 1")
    count = cursor.fetchone()[0]

    print(f"✅ CONEXIÓN EXITOSA!")
    print(f"   📡 Servidor: DESKTOP-OMLK3LH\\SQLKERSEYLOOR")
    print(f"   📊 Registros: {count} membresías")

    DatabaseConnection.cerrar_conexion()

except Exception as e:
    print(f"❌ Error SQL: {e}")

# Iniciar aplicación Qt
try:
    from PySide6.QtWidgets import QApplication
    from ui_qt.main_window_qt import MainWindowQt

    print("\n🎨 INICIANDO INTERFAZ Qt/PySide6...")

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    ventana = MainWindowQt()
    ventana.show()

    print("\n✅ INTERFAZ Qt INICIADA CORRECTAMENTE")
    print("📋 CARACTERÍSTICAS IMPLEMENTADAS:")
    print("   • Formulario completo con campos de membresía")
    print("   • Botones: Guardar, Buscar, Actualizar, Eliminar, Limpiar")
    print("   • Tabla QTableWidget para visualización")
    print("   • Mensajes QMessageBox para validaciones")
    print("   • Estilos CSS personalizados")
    print("   • Conexión a SQL Server 2022")


    sys.exit(app.exec())

except ImportError as e:
    print(f"\n❌ ERROR: {e}")
    print("\n⚠️  INSTALAR PySide6:")
    print("   pip install PySide6")
    input("\nPresiona Enter para salir...")
except Exception as e:
    print(f"\n❌ ERROR EJECUTANDO Qt: {e}")
    input("\nPresiona Enter para salir...")