import PyQt5
from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario de Registro")

        formulario_layout = qtw.QFormLayout()
        self.setLayout(formulario_layout)

        label_1 = qtw.QLabel("Presione el botón Registrarme luego de ingresar su Nombre")
        label_1.setFont(qtg.QFont("Arial", 12))

        nombre = qtw.QLineEdit(self)
        apellido = qtw.QLineEdit(self)

        formulario_layout.addRow(label_1)
        formulario_layout.addRow("Nombre", nombre)
        formulario_layout.addRow("Apellido", apellido)

        formulario_layout.addRow(qtw.QPushButton("Registrarme", clicked=lambda:press_it()))
        
        self.show()

        def press_it():
            label_1.setText(f"Listo! {nombre.text()} {apellido.text()}, estás oficialmente registrado \n en ESEN")

app = qtw.QApplication([])
mw = MainWindow()

app.exec()

