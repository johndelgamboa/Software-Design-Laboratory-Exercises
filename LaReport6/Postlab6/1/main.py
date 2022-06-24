from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys

class Tempe(QDialog):
    def __init__(self):
        super(Tempe, self).__init__()
        loadUi("C:/Users/User/Desktop/Postlab6/1/Temp.ui", self)
        self.celsius_input.setText("0.0")
        self.fahrenheit_input.setText("32.0")
        self.FartoCel.clicked.connect(self.fartocel)
        self.CeltoFar.clicked.connect(self.celtofar)

    def fartocel(self):
        fahr = self.fahrenheit_input.text()
        fahrr = float(fahr)


        celsius = round(cel, 4)

        print(f'{fahr} Fahrenheit to celcius: {celsius}')
        self.celsius_input.setText(str(celsius))

    def celtofar(self):
        cel = self.celsius_input.text()
        cels = float(cel)

        fahr = (9/5 * cels) + 32
        fahrenheit = round(fahr, 4)

        print(f'{cel} Celcius to Fahrenheit: {fahrenheit}' )
        self.fahrenheit_input.setText(str(fahrenheit))


app = QApplication(sys.argv)
mainwindow = Tempe()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("Converter")
widget.setFixedWidth(480)
widget.setFixedHeight(480)
widget.show()
app.exec_()
