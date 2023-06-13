# main.py

from PyQt6.QtWidgets import QApplication
from window import MainWindow
from twenty48 import Twenty48 as t48

app = QApplication([])

window = MainWindow()
window.show()

game = t48()
# Connect game signals/slots or interact with the window as needed

app.exec()
