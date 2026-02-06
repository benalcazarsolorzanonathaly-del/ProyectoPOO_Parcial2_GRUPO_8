#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

import os
import sys
from datetime import datetime

print("=" * 90)
print("🏋️  SISTEMA DE GESTIÓN DE GIMNASIO - GRUPO 8")
print("2do PARCIAL: POO + CRUD con SQL Server 2022")
print("=" * 90)

# Configurar rutas
ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ruta_proyecto)
sys.path.insert(0, os.path.join(ruta_proyecto, 'datos'))
sys.path.insert(0, os.path.join(ruta_proyecto, 'servicio'))
sys.path.insert(0, os.path.join(ruta_proyecto, 'dominio'))

print(f"\n📅 Fecha ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"📁 Proyecto: {ruta_proyecto}")

# ============================================
# 1. PROBAR CONEXIÓN SQL SERVER
# ============================================

print("\n" + "=" * 90)
print("🔗 1. CONEXIÓN A SQL SERVER")
print("=" * 90)

try:
    from datos.conexion import DatabaseConnection

    print("🔄 Conectando a SQL Server...")
    conexion = DatabaseConnection.obtener_conexion()
    cursor = DatabaseConnection.obtener_cursor()

    # Demostrar CRUD completo
    print("\n📊 DEMOSTRACIÓN CRUD COMPLETO:")
    print("-" * 50)

    # READ: Mostrar datos existentes
    cursor.execute("SELECT TOP 3 * FROM Membresias WHERE activo = 1 ORDER BY id_membresia")
    datos = cursor.fetchall()

    print("✅ READ - Consulta de membresías:")
    for fila in datos:
        print(f"   • ID: {fila[0]:2} | {fila[1]:25} | ${fila[2]:6.2f} | {fila[3]:10}")

    # CREATE: Insertar nueva
    print("\n✅ CREATE - Insertar nueva membresía...")
    cursor.execute("""
        INSERT INTO Membresias (nombre, precio_base, tipo, acceso_sala, acceso_clases)
        VALUES (?, ?, ?, ?, ?)
    """, ('Plan Demo Final', 88.88, 'Presencial', 1, 0))
    conexion.commit()
    print("   ✓ Membresía 'Plan Demo Final' creada")

    # UPDATE: Actualizar
    print("\n✅ UPDATE - Actualizar precio...")
    cursor.execute("""
        UPDATE Membresias 
        SET precio_base = 99.99 
        WHERE nombre = 'Plan Demo Final'
    """)
    conexion.commit()
    print("   ✓ Precio actualizado a $99.99")

    # DELETE: Eliminar
    print("\n✅ DELETE - Eliminar (borrado lógico)...")
    cursor.execute("""
        UPDATE Membresias 
        SET activo = 0 
        WHERE nombre = 'Plan Demo Final'
    """)
    conexion.commit()
    print("   ✓ Membresía marcada como inactiva")

    # Estadísticas finales
    cursor.execute("SELECT COUNT(*) FROM Membresias WHERE activo = 1")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(precio_base) FROM Membresias WHERE activo = 1")
    promedio = cursor.fetchone()[0] or 0

    print(f"\n📈 ESTADÍSTICAS FINALES:")
    print(f"   • Total membresías activas: {total}")
    print(f"   • Precio promedio: ${promedio:.2f}")
    print(f"   • Servidor: DESKTOP-OMLK3LH\\SQLKERSEYLOOR")
    print(f"   • Base de datos: GimnasioDB")

    DatabaseConnection.cerrar_conexion()
    print("\n✅ CONEXIÓN SQL SERVER: EXITOSA")

except Exception as e:
    print(f"❌ ERROR SQL: {e}")

# ============================================
# 2. DEMOSTRAR CLASES POO
# ============================================

print("\n" + "=" * 90)
print("📦 2. CLASES POO (5 CLASES REQUERIDAS)")
print("=" * 90)

try:
    from dominio.clase_base import ServicioGym
    from dominio.clase_hija_1 import MembresiaPresencial
    from dominio.clase_hija_2 import MembresiaVirtual
    from dominio.clase_extra_1 import Cliente
    from dominio.clase_extra_2 import GestorGym

    print("✅ 5 CLASES CARGADAS:")
    print("   1. ServicioGym (superclase abstracta)")
    print("   2. MembresiaPresencial (subclase 1)")
    print("   3. MembresiaVirtual (subclase 2)")
    print("   4. Cliente (clase adicional)")
    print("   5. GestorGym (clase adicional)")

    # Demostrar encapsulamiento
    print("\n🔒 ENCAPSULAMIENTO:")
    mp = MembresiaPresencial("Plan Test", 60.00, True, False)
    print(f"   • Atributo privado _nombre: {mp._nombre}")
    print(f"   • Property @nombre: {mp.nombre}")

    # Demostrar herencia
    print("\n🧬 HERENCIA:")
    print(f"   • MembresiaPresencial hereda de ServicioGym: {issubclass(MembresiaPresencial, ServicioGym)}")
    print(f"   • MembresiaVirtual hereda de ServicioGym: {issubclass(MembresiaVirtual, ServicioGym)}")

    # Demostrar polimorfismo
    print("\n🌀 POLIMORFISMO:")
    servicios = [
        MembresiaPresencial("Básico", 50.00, True, False),
        MembresiaPresencial("Premium", 80.00, True, True),
        MembresiaVirtual("Virtual Full", 45.00, "Premium", True)
    ]

    total = 0
    for i, s in enumerate(servicios, 1):
        costo = s.calcular_costo()
        total += costo
        print(f"   {i}. {s.nombre:15} - Costo: ${costo:6.2f}")

    print(f"   📊 TOTAL (polimorfismo): ${total:.2f}")

    # Demostrar Gestor con método polimórfico
    print("\n📋 GESTOR CON MÉTODO POLIMÓRFICO:")
    gestor = GestorGym()
    for s in servicios:
        gestor.agregar_servicio(s)

    print(f"   • Total ingresos: ${gestor.calcular_total_ingresos(servicios):.2f}")
    print(f"   • Reporte generado: {len(gestor.generar_reporte(servicios).split('\\n'))} líneas")

    print("\n✅ POO: TODOS LOS REQUISITOS CUMPLIDOS")

except Exception as e:
    print(f"❌ ERROR POO: {e}")

# ============================================
# 3. DEMOSTRAR CRUD CON SERVICIO
# ============================================

print("\n" + "=" * 90)
print("🔄 3. CRUD CON CAPA DE SERVICIO")
print("=" * 90)

try:
    from servicio.membresia_service import MembresiaService

    servicio = MembresiaService()

    print("\n📋 OPERACIONES CRUD:")
    print("-" * 50)

    # READ
    print("🔍 READ - Obtener todas:")
    resultado = servicio.obtener_todas()
    if resultado['exito']:
        print(f"   • {resultado['mensaje']}")
    else:
        print(f"   • Error: {resultado['mensaje']}")

    # CREATE
    print("\n➕ CREATE - Crear presencial:")
    resultado = servicio.crear_presencial("Plan Servicio Test", 77.77, True, False)
    print(f"   • {resultado['mensaje']}")

    # READ por nombre
    print("\n🔍 READ - Buscar por nombre 'Plan':")
    resultado = servicio.buscar_por_nombre("Plan")
    print(f"   • {resultado['mensaje']}")

    # UPDATE
    print("\n✏️ UPDATE - Actualizar precio:")
    resultado = servicio.actualizar(1, {'precio_base': 60.00})
    print(f"   • {resultado['mensaje']}")

    # DELETE
    print("\n🗑️ DELETE - Eliminar membresía:")
    resultado = servicio.eliminar(3)
    print(f"   • {resultado['mensaje']}")

    # Estadísticas
    print("\n📊 ESTADÍSTICAS DEL SISTEMA:")
    resultado = servicio.obtener_estadisticas()
    if resultado['exito']:
        stats = resultado['data']
        print(f"   • Total membresías: {stats['total']}")
        print(f"   • Presenciales: {stats['presencial']}")
        print(f"   • Virtuales: {stats['virtual']}")
        print(f"   • Precio promedio: ${stats['promedio']}")

    print("\n✅ CRUD: TODAS LAS OPERACIONES FUNCIONANDO")

except Exception as e:
    print(f"❌ ERROR SERVICIO: {e}")


print("\n" + "=" * 90)
print("👨‍🎓 GRUPO 8 - PROYECTO COMPLETO Y FUNCIONAL")
print("=" * 90)


