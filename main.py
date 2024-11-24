import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel,
    QGroupBox, QScrollArea, QFormLayout, QListWidget, QAbstractItemView, QMessageBox, QSpinBox,
)
from Sandwich import Pavo, Pollo, Beef, Italiano, Veggie, Atun, Combo
from Decoradores import Aguacate, DobleProteina, Hongos, Refresco, Sopa, Postre
from PyQt6.QtGui import QIcon
import os


class Visual(QWidget):
    def __init__(self):
        super().__init__()

        # Lista de sándwiches en la orden
        self.orden = []
        self.precio_total = 0.0
        self.ico = os.path.join("Imagenes", "sub.ico")
        self.setWindowIcon(QIcon(self.ico))
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sistema de Pedido de Sándwiches")
        self.setGeometry(200, 200, 800, 600)

        main_layout = QVBoxLayout()

        # Título principal
        title_label = QLabel("¡Bienvenido al sistema de Sándwiches!")
        main_layout.addWidget(title_label)

        # Área de scroll para agregar sándwiches
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        # Combo box para seleccionar tipo de sándwich
        self.sandwich_combo = QComboBox(self)
        self.sandwich_combo.addItems(["Pavo", "Pollo", "Beef", "Italiano", "Veggie", "Atún"])
        self.scroll_layout.addWidget(QLabel("Selecciona el tipo de sándwich:"))
        self.scroll_layout.addWidget(self.sandwich_combo)

        # Combo box para seleccionar tamaño
        self.size_combo = QComboBox(self)
        self.size_combo.addItems(["15 cm", "30 cm"])
        self.scroll_layout.addWidget(QLabel("Selecciona el tamaño:"))
        self.scroll_layout.addWidget(self.size_combo)

        # Combo box para seleccionar un combo
        self.combo_sandwich_combo = QComboBox(self)
        self.combo_sandwich_combo.addItems(["", "Pavo + Pollo", "Beef + Italiano", "Veggie + Atún"])
        self.scroll_layout.addWidget(QLabel("Selecciona un combo (opcional):"))
        self.scroll_layout.addWidget(self.combo_sandwich_combo)

        # Botón para agregar un sándwich o combo
        add_sandwich_button = QPushButton("Agregar Sándwich/Combo", self)
        add_sandwich_button.clicked.connect(self.agregarSandwich)
        self.scroll_layout.addWidget(add_sandwich_button)

        # Botón para agregar adicionales
        add_adicional_button = QPushButton("Agregar Adicionales", self)
        add_adicional_button.clicked.connect(self.agregarAdicionales)
        self.scroll_layout.addWidget(add_adicional_button)

        self.scroll_area.setWidget(self.scroll_widget)
        main_layout.addWidget(self.scroll_area)

        # Lista para mostrar los sándwiches de la orden
        self.order_list = QListWidget()
        self.order_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        main_layout.addWidget(QLabel("Orden actual:"))
        main_layout.addWidget(self.order_list)

        # Botón para eliminar sándwiches seleccionados
        remove_button = QPushButton("Eliminar Sándwich(es)", self)
        remove_button.clicked.connect(self.eliminarSandwich)
        main_layout.addWidget(remove_button)

        # Checkboxes para los adicionales
        adicionales_group = QGroupBox("Adicionales disponibles:")
        adicionales_layout = QFormLayout()

        # Cambié los Checkboxes por SpinBoxes
        self.spin_aguacate = self.agregarSpinBox("Aguacate", adicionales_layout)
        self.spin_doble_proteina = self.agregarSpinBox("Doble Proteína", adicionales_layout)
        self.spin_hongos = self.agregarSpinBox("Hongos", adicionales_layout)
        self.spin_refresco = self.agregarSpinBox("Refresco", adicionales_layout)
        self.spin_sopa = self.agregarSpinBox("Sopa", adicionales_layout)
        self.spin_postre = self.agregarSpinBox("Postre", adicionales_layout)

        adicionales_group.setLayout(adicionales_layout)
        main_layout.addWidget(adicionales_group)

        # Etiqueta para mostrar el precio total
        self.price_label = QLabel(f"Precio Total: ${self.precio_total:.2f}")
        main_layout.addWidget(self.price_label)

        # Botón para confirmar la orden
        confirm_button = QPushButton("Confirmar Orden", self)
        confirm_button.clicked.connect(self.confirmarOrden)
        main_layout.addWidget(confirm_button)

        self.setLayout(main_layout)

    def agregarSpinBox(self, label, layout):
        spin_box = QSpinBox(self)
        spin_box.setRange(0, 10)  # Establecer el rango de repeticiones
        layout.addRow(f"{label}:", spin_box)
        return spin_box

    def obtenerAdicionales(self):
        """
        Obtiene los decoradores seleccionados por el usuario y los aplica al último sándwich.
        """
        if not self.orden:
            QMessageBox.warning(self, "Error", "Primero debes agregar un sándwich.")
            return None

        # Tomar el último sándwich agregado
        sandwich_base = self.orden[-1]["sandwich"]

        # Aplicar adicionales seleccionados como decoradores
        for _ in range(self.spin_aguacate.value()):
            sandwich_base = Aguacate(sandwich_base)
        for _ in range(self.spin_doble_proteina.value()):
            sandwich_base = DobleProteina(sandwich_base)
        for _ in range(self.spin_hongos.value()):
            sandwich_base = Hongos(sandwich_base)
        for _ in range(self.spin_refresco.value()):
            sandwich_base = Refresco(sandwich_base)
        for _ in range(self.spin_sopa.value()):
            sandwich_base = Sopa(sandwich_base)
        for _ in range(self.spin_postre.value()):
            sandwich_base = Postre(sandwich_base)

        return sandwich_base


    def agregarSandwich(self):
        """
        Agrega un nuevo sándwich a la orden, aplicando los adicionales seleccionados.
        """
        # Obtener tipo y tamaño seleccionados
        tipo = self.sandwich_combo.currentText()
        tamaño = 15 if self.size_combo.currentIndex() == 0 else 30

        # Comprobar si se seleccionó un combo
        combo = self.combo_sandwich_combo.currentText()
        if combo:
            tipo1, tipo2 = combo.split(" + ")
            sandwich = Combo(tipo1, tipo2, tamaño)
        else:
            sandwich = self.crearSandwich(tipo, tamaño)

        # Añadir a la orden temporal (para agregar los adicionales)
        self.orden.append({"sandwich": sandwich, "adicionales": []})

        self.actualizarOrden()

    def agregarAdicionales(self):
        """
        Agrega los adicionales seleccionados al último sándwich de la orden.
        """
        if not self.orden:
            QMessageBox.warning(self, "Error", "Primero debes agregar un sándwich.")
            return

        # Obtener el sándwich actualizado con adicionales
        sandwich_con_adicionales = self.obtenerAdicionales()

        if sandwich_con_adicionales:
            # Actualizar el último elemento de la orden con los adicionales aplicados
            self.orden[-1]["sandwich"] = sandwich_con_adicionales

            # Limpiar los SpinBoxes
            self.spin_aguacate.setValue(0)
            self.spin_doble_proteina.setValue(0)
            self.spin_hongos.setValue(0)
            self.spin_refresco.setValue(0)
            self.spin_sopa.setValue(0)
            self.spin_postre.setValue(0)

            # Actualizar la lista visual
            self.actualizarOrden()



    def crearSandwich(self, tipo, tamaño):
        """
        Crea un objeto de sándwich según el tipo y tamaño seleccionados.
        """
        if tipo == "Pavo":
            return Pavo(tamaño)
        elif tipo == "Pollo":
            return Pollo(tamaño)
        elif tipo == "Beef":
            return Beef(tamaño)
        elif tipo == "Italiano":
            return Italiano(tamaño)
        elif tipo == "Veggie":
            return Veggie(tamaño)
        elif tipo == "Atún":
            return Atun(tamaño)

    def actualizarOrden(self):
        """
        Actualiza la lista de sándwiches en la interfaz y recalcula el precio total.
        """
        self.order_list.clear()
        self.precio_total = 0.0

        # Mostrar cada sándwich y calcular el precio total
        for item in self.orden:
            sandwich = item["sandwich"]
            descripcion = sandwich.getDescripcion()
            precio = sandwich.getPrecio()

            # Agregar a la lista visual
            self.order_list.addItem(f"{descripcion} PRECIO ${precio:.2f}")
            self.precio_total += precio

        # Actualizar la etiqueta de precio total
        self.price_label.setText(f"Precio Total: ${self.precio_total:.2f}")


    def eliminarSandwich(self):
        """
        Elimina los sándwiches seleccionados de la orden.
        """
        selected_items = self.order_list.selectedItems()

        if not selected_items:
            QMessageBox.warning(self, "Error", "No has seleccionado ningún sándwich para eliminar.")
            return

        # List to store the indices of sandwiches to remove
        indices_to_remove = []

        # Recorremos los elementos seleccionados en la UI
        for item in selected_items:
            # Buscamos el sándwich correspondiente en la lista de la orden
            for idx, sandwich_entry in enumerate(self.orden):
                sandwich = sandwich_entry["sandwich"]
                adicionales = sandwich_entry["adicionales"]

                # Crear una representación completa del sándwich con sus adicionales
                descripcion_sandwich = sandwich.getDescripcion()
                detalles_adicionales = [adicional.getDescripcion() for adicional in adicionales]
                descripcion_completa = descripcion_sandwich + (" + " + " + ".join(detalles_adicionales) if detalles_adicionales else "")

                # Compara con el texto de la UI (sólo la descripción sin el precio)
                if descripcion_completa.strip() == item.text().split(' PRECIO')[0].strip():
                    indices_to_remove.append(idx)
                    break

        # Eliminamos los elementos desde el último hacia el primero (para evitar problemas al eliminar)
        for idx in sorted(indices_to_remove, reverse=True):
            del self.orden[idx]

        # Actualizamos la interfaz de la orden después de la eliminación
        self.actualizarOrden()



    def confirmarOrden(self):
        """
        Confirma la orden, mostrando un resumen detallado y luego limpia la lista de la orden.
        """
        if not self.orden:
            QMessageBox.warning(self, "Error", "No has agregado ningún sándwich.")
            return

        # Crear el resumen de la orden
        resumen = "\n".join(
            [f"{sandwich['sandwich'].getDescripcion()} PRECIO ${sandwich['sandwich'].getPrecio():.2f}" for sandwich in self.orden]
        )

        # Mostrar el resumen
        QMessageBox.information(self, "Orden Confirmada",
                                f"Resumen de tu orden:\n\n{resumen}\n\nPrecio Total: ${self.precio_total:.2f}")

        # Limpiar la orden
        self.orden.clear()
        self.order_list.clear()
        self.precio_total = 0.0
        self.price_label.setText(f"Precio Total: ${self.precio_total:.2f}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Visual()
    ventana.show()
    sys.exit(app.exec())
