import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QImage, QPixmap

def hacer_clic():
    etiqueta.setText("¡Hiciste clic en la imagen!")

app = QApplication(sys.argv)
ventana = QMainWindow()
ventana.setWindowTitle("PUÑOGRANADA")
ventana.setFixedSize(800, 533)

imagen_fondo = QImage("C:\\Users\\Practica\\Desktop\\game\\fondo_puño.png")
etiqueta_fondo = QLabel(ventana)
etiqueta_fondo.setPixmap(QPixmap.fromImage(imagen_fondo))
etiqueta_fondo.setGeometry(0, 0, 800, 533)

etiqueta = QLabel(ventana)
etiqueta.setText("Hola, PyQt5")
etiqueta.move(10, 10)

imagen = QImage("boton_jugar.png")
imagen = imagen.scaled(200, 100)
imagen_tk = QPixmap.fromImage(imagen)

etiqueta_imagen = QLabel(ventana)
etiqueta_imagen.setPixmap(imagen_tk)
etiqueta_imagen.setGeometry(300, 350, 200, 100)
etiqueta_imagen.mousePressEvent = hacer_clic

ventana.show()
sys.exit(app.exec_())
