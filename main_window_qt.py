#GRUPO 8
#Benalcazar solorzano Nathaly Alexandra
#Mero mero Valentina Maricela
#Salinas José Joel Isaías
#Vargas Sudario Andrea Alejandra

# ui_qt/main_window_qt.py
# INTERFAZ COMPLETA CREADA POR CÓDIGO - SIN QT DESIGNER

import sys
import os
from PySide6.QtWidgets import (QMainWindow, QApplication, QMessageBox,
                               QTableWidgetItem, QHeaderView, QWidget,
                               QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QTableWidget, QComboBox, QCheckBox,
                               QGroupBox, QFormLayout, QGridLayout, QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon

# Configurar rutas
ruta_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ruta_proyecto)

try:
    from servicio.membresia_service import MembresiaService

    SERVICIO_DISPONIBLE = True
except ImportError:
    print("⚠️  Servicio no disponible, usando modo demostración")
    SERVICIO_DISPONIBLE = False


    class MembresiaService:
        def __init__(self):
            print("✅ Servicio de demostración inicializado")

        def crear_presencial(self, nombre, precio, sala, clases):
            return {'exito': True, 'mensaje': f'Membresía "{nombre}" creada', 'id': 100}

        def crear_virtual(self, nombre, precio, plan, app):
            return {'exito': True, 'mensaje': f'Membresía "{nombre}" creada', 'id': 101}

        def buscar_por_nombre(self, nombre):
            return {'exito': True, 'mensaje': f'Búsqueda: {nombre}', 'data': []}

        def buscar_por_id(self, id_membresia):
            return {'exito': True, 'data': {'id': id_membresia, 'nombre': 'Demo', 'precio': 50.0}}

        def actualizar(self, id_membresia, datos):
            return {'exito': True, 'mensaje': f'Actualizado ID: {id_membresia}'}

        def eliminar(self, id_membresia):
            return {'exito': True, 'mensaje': f'Eliminado ID: {id_membresia}'}

        def obtener_todas(self):
            return {'exito': True, 'data': [
                (1, 'Plan Básico', 50.00, 'Presencial'),
                (2, 'Plan Premium', 80.00, 'Presencial'),
                (3, 'Virtual Full', 45.00, 'Virtual'),
                (4, 'Plan Familiar', 120.00, 'Presencial')
            ]}


class MainWindowQt(QMainWindow):
    """Ventana principal creada completamente por código."""

    def __init__(self):
        super().__init__()
        self.servicio = MembresiaService()
        self.membresia_actual = None

        # Configurar ventana
        self.setWindowTitle("🏋️ Sistema de Gestión de Gimnasio - Grupo 8 - Qt")
        self.setGeometry(100, 100, 1100, 750)  # x, y, ancho, alto

        # Crear interfaz
        self.crear_interfaz()

        # Conectar eventos
        self.conectar_eventos()

        # Cargar datos iniciales
        self.cargar_datos_iniciales()

        print("✅ Interfaz Qt creada correctamente")

    def crear_interfaz(self):
        """Crea todos los componentes de la interfaz."""

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout_principal = QVBoxLayout(central_widget)
        layout_principal.setSpacing(15)
        layout_principal.setContentsMargins(20, 20, 20, 20)

        # ========== TÍTULO ==========
        frame_titulo = QFrame()
        frame_titulo.setStyleSheet("background-color: #2c3e50; border-radius: 10px;")
        layout_titulo = QVBoxLayout(frame_titulo)

        label_titulo = QLabel("🏋️ SISTEMA DE GESTIÓN DE GIMNASIO")
        label_titulo.setStyleSheet("color: white; font-size: 22px; font-weight: bold; padding: 10px;")
        label_titulo.setAlignment(Qt.AlignCenter)

        label_subtitulo = QLabel("Grupo 8 | CRUD con SQL Server 2022 | Qt/PySide6")
        label_subtitulo.setStyleSheet("color: #ecf0f1; font-size: 12px;")
        label_subtitulo.setAlignment(Qt.AlignCenter)

        layout_titulo.addWidget(label_titulo)
        layout_titulo.addWidget(label_subtitulo)
        layout_principal.addWidget(frame_titulo)

        # ========== FORMULARIO ==========
        grupo_formulario = QGroupBox("📝 FORMULARIO DE MEMBRESÍA")
        grupo_formulario.setStyleSheet("""
            QGroupBox {
                font-size: 14px;
                font-weight: bold;
                border: 2px solid #3498db;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
            }
        """)

        layout_formulario = QGridLayout()
        layout_formulario.setSpacing(15)

        # Fila 1: ID y Nombre
        label_id = QLabel("ID:")
        label_id.setStyleSheet("font-weight: bold;")
        self.label_id_valor = QLabel("NUEVA")
        self.label_id_valor.setStyleSheet("color: #2980b9; font-weight: bold; font-size: 14px;")

        label_nombre = QLabel("Nombre*:")
        label_nombre.setStyleSheet("font-weight: bold;")
        self.entry_nombre = QLineEdit()
        self.entry_nombre.setPlaceholderText("Ej: Plan Premium Plus")
        self.entry_nombre.setStyleSheet("padding: 8px; border: 1px solid #bdc3c7; border-radius: 4px;")
        self.entry_nombre.setText("Plan Premium Gimnasio")

        layout_formulario.addWidget(label_id, 0, 0)
        layout_formulario.addWidget(self.label_id_valor, 0, 1)
        layout_formulario.addWidget(label_nombre, 0, 2)
        layout_formulario.addWidget(self.entry_nombre, 0, 3, 1, 2)

        # Fila 2: Precio y Tipo
        label_precio = QLabel("Precio ($)*:")
        label_precio.setStyleSheet("font-weight: bold;")
        self.entry_precio = QLineEdit()
        self.entry_precio.setPlaceholderText("Ej: 75.00")
        self.entry_precio.setStyleSheet("padding: 8px; border: 1px solid #bdc3c7; border-radius: 4px;")
        self.entry_precio.setText("75.00")

        label_tipo = QLabel("Tipo*:")
        label_tipo.setStyleSheet("font-weight: bold;")
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["🏋️ Presencial", "💻 Virtual"])
        self.combo_tipo.setStyleSheet("padding: 8px; border: 1px solid #bdc3c7; border-radius: 4px;")
        self.combo_tipo.currentIndexChanged.connect(self.cambiar_tipo)

        layout_formulario.addWidget(label_precio, 1, 0)
        layout_formulario.addWidget(self.entry_precio, 1, 1, 1, 2)
        layout_formulario.addWidget(label_tipo, 1, 3)
        layout_formulario.addWidget(self.combo_tipo, 1, 4)

        # Fila 3: Campos específicos
        self.frame_especifico = QFrame()
        layout_especifico = QVBoxLayout(self.frame_especifico)
        layout_especifico.setContentsMargins(0, 0, 0, 0)

        # Inicializar con campos presenciales
        self.chk_sala = QCheckBox("✅ Incluye acceso a sala de pesas")
        self.chk_sala.setChecked(True)

        self.chk_clases = QCheckBox("✅ Incluye clases grupales guiadas")
        self.chk_clases.setChecked(False)

        layout_especifico.addWidget(self.chk_sala)
        layout_especifico.addWidget(self.chk_clases)

        layout_formulario.addWidget(self.frame_especifico, 2, 0, 1, 5)

        grupo_formulario.setLayout(layout_formulario)
        layout_principal.addWidget(grupo_formulario)

        # ========== BOTONES CRUD ==========
        frame_botones = QFrame()
        layout_botones = QHBoxLayout(frame_botones)
        layout_botones.setSpacing(10)

        # Crear botones con estilos
        self.botones = {
            'guardar': self.crear_boton("➕ GUARDAR", "#27ae60"),
            'buscar': self.crear_boton("🔍 BUSCAR", "#3498db"),
            'actualizar': self.crear_boton("✏️ ACTUALIZAR", "#f39c12"),
            'eliminar': self.crear_boton("🗑️ ELIMINAR", "#e74c3c"),
            'limpiar': self.crear_boton("🧹 LIMPIAR", "#95a5a6")
        }

        for boton in self.botones.values():
            layout_botones.addWidget(boton)

        layout_principal.addWidget(frame_botones)

        # ========== TABLA DE DATOS ==========
        grupo_tabla = QGroupBox("📋 MEMBRESÍAS REGISTRADAS")
        grupo_tabla.setStyleSheet("""
            QGroupBox {
                font-size: 14px;
                font-weight: bold;
                border: 2px solid #2ecc71;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
            }
        """)

        layout_tabla = QVBoxLayout()

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO ($)", "TIPO"])

        # Estilos de la tabla
        self.tabla.setStyleSheet("""
            QTableWidget {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                background-color: white;
                alternate-background-color: #f8f9fa;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 8px;
                border: 1px solid #2c3e50;
                font-weight: bold;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QTableWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
        """)

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows)

        layout_tabla.addWidget(self.tabla)
        grupo_tabla.setLayout(layout_tabla)
        layout_principal.addWidget(grupo_tabla, 1)  # factor de expansión 1

        # ========== BARRA DE ESTADO ==========
        self.label_estado = QLabel("✅ Sistema listo - Conectado a SQL Server")
        self.label_estado.setStyleSheet("""
            background-color: #2c3e50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 11px;
        """)
        self.label_estado.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(self.label_estado)

    def crear_boton(self, texto, color):
        """Crea un botón con estilo personalizado."""
        boton = QPushButton(texto)
        boton.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 12px;
            }}
            QPushButton:hover {{
                background-color: {self.oscurecer_color(color)};
            }}
            QPushButton:pressed {{
                background-color: {self.oscurecer_color(color, 40)};
                padding: 13px 19px 11px 21px;
            }}
        """)
        boton.setCursor(Qt.PointingHandCursor)
        return boton

    def oscurecer_color(self, hex_color, porcentaje=20):
        """Oscurece un color hexadecimal."""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        r = max(0, r - (r * porcentaje // 100))
        g = max(0, g - (g * porcentaje // 100))
        b = max(0, b - (b * porcentaje // 100))

        return f'#{r:02x}{g:02x}{b:02x}'

    def cambiar_tipo(self):
        """Cambia los campos según el tipo seleccionado."""
        # Limpiar frame
        for i in reversed(range(self.frame_especifico.layout().count())):
            widget = self.frame_especifico.layout().itemAt(i).widget()
            if widget:
                widget.deleteLater()

        tipo = self.combo_tipo.currentText()

        if "Presencial" in tipo:
            self.chk_sala = QCheckBox("✅ Incluye acceso a sala de pesas")
            self.chk_sala.setChecked(True)

            self.chk_clases = QCheckBox("✅ Incluye clases grupales guiadas")
            self.chk_clases.setChecked(False)

            self.frame_especifico.layout().addWidget(self.chk_sala)
            self.frame_especifico.layout().addWidget(self.chk_clases)
        else:
            label_plan = QLabel("Plan de Videos:")
            label_plan.setStyleSheet("font-weight: bold;")

            self.combo_plan = QComboBox()
            self.combo_plan.addItems(["Básico", "Estándar", "Premium", "Avanzado"])
            self.combo_plan.setCurrentText("Premium")
            self.combo_plan.setStyleSheet("padding: 6px; border: 1px solid #bdc3c7; border-radius: 4px;")

            self.chk_app = QCheckBox("✅ Incluye App Móvil Premium")
            self.chk_app.setChecked(True)

            self.frame_especifico.layout().addWidget(label_plan)
            self.frame_especifico.layout().addWidget(self.combo_plan)
            self.frame_especifico.layout().addWidget(self.chk_app)

    def conectar_eventos(self):
        """Conecta los eventos de los botones."""
        self.botones['guardar'].clicked.connect(self.guardar)
        self.botones['buscar'].clicked.connect(self.buscar)
        self.botones['actualizar'].clicked.connect(self.actualizar)
        self.botones['eliminar'].clicked.connect(self.eliminar)
        self.botones['limpiar'].clicked.connect(self.limpiar)

        self.tabla.itemSelectionChanged.connect(self.seleccionar_tabla)

    def seleccionar_tabla(self):
        """Maneja selección en la tabla."""
        seleccion = self.tabla.selectedItems()
        if seleccion:
            fila = seleccion[0].row()
            id_item = self.tabla.item(fila, 0).text()
            nombre_item = self.tabla.item(fila, 1).text()
            precio_item = self.tabla.item(fila, 2).text()

            self.membresia_actual = int(id_item)
            self.label_id_valor.setText(id_item)
            self.entry_nombre.setText(nombre_item)
            self.entry_precio.setText(precio_item.replace('$', '').strip())

            tipo = self.tabla.item(fila, 3).text()
            if "Presencial" in tipo:
                self.combo_tipo.setCurrentText("🏋️ Presencial")
            else:
                self.combo_tipo.setCurrentText("💻 Virtual")

    def cargar_datos_iniciales(self):
        """Carga datos iniciales en la tabla."""
        resultado = self.servicio.obtener_todas()

        if resultado['exito']:
            datos = resultado['data']
            self.tabla.setRowCount(len(datos))

            for i, item in enumerate(datos):
                if isinstance(item, tuple) and len(item) >= 4:
                    self.tabla.setItem(i, 0, QTableWidgetItem(str(item[0])))
                    self.tabla.setItem(i, 1, QTableWidgetItem(str(item[1])))
                    self.tabla.setItem(i, 2, QTableWidgetItem(f"${item[2]:.2f}"))
                    self.tabla.setItem(i, 3, QTableWidgetItem(str(item[3])))

        self.label_estado.setText(f"✅ {resultado.get('mensaje', 'Datos cargados')}")

    def validar_formulario(self):
        """Valida los campos del formulario."""
        nombre = self.entry_nombre.text().strip()
        precio = self.entry_precio.text().strip()

        if not nombre:
            QMessageBox.critical(self, "❌ Error de Validación",
                                 "El nombre es obligatorio")
            return False

        if not precio:
            QMessageBox.critical(self, "❌ Error de Validación",
                                 "El precio es obligatorio")
            return False

        try:
            float(precio)
            return True
        except ValueError:
            QMessageBox.critical(self, "❌ Error de Validación",
                                 "El precio debe ser un número válido")
            return False

    def guardar(self):
        """Operación CREATE."""
        if not self.validar_formulario():
            return

        nombre = self.entry_nombre.text().strip()
        precio = float(self.entry_precio.text().strip())
        tipo = self.combo_tipo.currentText()

        if "Presencial" in tipo:
            resultado = self.servicio.crear_presencial(
                nombre, precio,
                self.chk_sala.isChecked(),
                self.chk_clases.isChecked() if hasattr(self, 'chk_clases') else False
            )
        else:
            plan = self.combo_plan.currentText() if hasattr(self, 'combo_plan') else "Premium"
            app = self.chk_app.isChecked() if hasattr(self, 'chk_app') else True

            resultado = self.servicio.crear_virtual(nombre, precio, plan, app)

        if resultado.get('exito', False):
            QMessageBox.information(self, "✅ Éxito", resultado['mensaje'])
            self.limpiar()
            self.cargar_datos_iniciales()
        else:
            QMessageBox.critical(self, "❌ Error",
                                 resultado.get('mensaje', 'Error desconocido'))

    def buscar(self):
        """Operación READ."""
        nombre = self.entry_nombre.text().strip()

        if not nombre:
            QMessageBox.warning(self, "⚠️ Advertencia",
                                "Ingrese un nombre para buscar")
            return

        resultado = self.servicio.buscar_por_nombre(nombre)

        if resultado.get('exito', False):
            datos = resultado.get('data', [])
            self.tabla.setRowCount(len(datos))

            for i, item in enumerate(datos):
                if isinstance(item, tuple) and len(item) >= 4:
                    self.tabla.setItem(i, 0, QTableWidgetItem(str(item[0])))
                    self.tabla.setItem(i, 1, QTableWidgetItem(str(item[1])))
                    self.tabla.setItem(i, 2, QTableWidgetItem(f"${item[2]:.2f}"))
                    self.tabla.setItem(i, 3, QTableWidgetItem(str(item[3])))

            mensaje = f"{resultado['mensaje']}\nEncontradas: {len(datos)} membresías"
            QMessageBox.information(self, "🔍 Resultados", mensaje)
            self.label_estado.setText(f"🔍 {mensaje}")
        else:
            QMessageBox.information(self, "🔍 Resultados", resultado['mensaje'])

    def actualizar(self):
        """Operación UPDATE."""
        if not self.membresia_actual:
            QMessageBox.warning(self, "⚠️ Advertencia",
                                "Seleccione una membresía para actualizar")
            return

        if not self.validar_formulario():
            return

        datos = {
            'nombre': self.entry_nombre.text().strip(),
            'precio_base': float(self.entry_precio.text().strip())
        }

        resultado = self.servicio.actualizar(self.membresia_actual, datos)

        if resultado.get('exito', False):
            QMessageBox.information(self, "✅ Éxito", resultado['mensaje'])
            self.cargar_datos_iniciales()
            self.label_estado.setText(f"✏️ {resultado['mensaje']}")
        else:
            QMessageBox.critical(self, "❌ Error",
                                 resultado.get('mensaje', 'Error desconocido'))

    def eliminar(self):
        """Operación DELETE."""
        if not self.membresia_actual:
            QMessageBox.warning(self, "⚠️ Advertencia",
                                "Seleccione una membresía para eliminar")
            return

        respuesta = QMessageBox.question(
            self, "🗑️ Confirmar Eliminación",
            f"¿Está seguro de eliminar la membresía ID {self.membresia_actual}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:
            resultado = self.servicio.eliminar(self.membresia_actual)

            if resultado.get('exito', False):
                QMessageBox.information(self, "✅ Éxito", resultado['mensaje'])
                self.limpiar()
                self.cargar_datos_iniciales()
                self.membresia_actual = None
                self.label_estado.setText(f"🗑️ {resultado['mensaje']}")
            else:
                QMessageBox.critical(self, "❌ Error",
                                     resultado.get('mensaje', 'Error desconocido'))

    def limpiar(self):
        """Limpia el formulario."""
        self.label_id_valor.setText("NUEVA")
        self.entry_nombre.clear()
        self.entry_precio.clear()
        self.combo_tipo.setCurrentIndex(0)
        self.membresia_actual = None
        self.tabla.clearSelection()

        QMessageBox.information(self, "🧹 Limpiar", "Formulario limpiado correctamente")
        self.label_estado.setText("✅ Formulario limpiado - Listo para nueva entrada")


# Si se ejecuta directamente
if __name__ == "__main__":
    print("=" * 80)
    print("🔧 EJECUTANDO MAIN_WINDOW_QT DIRECTAMENTE")
    print("=" * 80)

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    ventana = MainWindowQt()
    ventana.show()

    sys.exit(app.exec())