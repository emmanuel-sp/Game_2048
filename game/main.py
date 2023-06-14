# main.py

from twenty48 import Twenty48 as t48

from PyQt6.QtWidgets import QApplication, QGraphicsView
from PyQt6.QtCore import Qt
from window import GraphicsScene

app = QApplication([])

scene = GraphicsScene()
view = QGraphicsView(scene)
view.setAlignment(Qt.AlignmentFlag.AlignBottom)

view.setWindowTitle("Game 2048")
view.setFixedSize(550, 630)
view.show()

game = t48()

app.exec()
