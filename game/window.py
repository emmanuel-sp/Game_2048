# window.py

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QIcon, QColor, QFont
from PyQt6.QtCore import  QSize, Qt, QRect, QRectF, QPointF

font = QFont("Clear Sans", 35, QFont.Weight.Bold)
class GraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 500, 500) # Set the scene rectangle size
        rectangles = []
        texts = []
        self.addText("2048", QFont("Clear Sans", 50, QFont.Weight.Bold)).setPos(10, 10)
        
        for row in range(4):
            rectangles.append([])
            texts.append([])
            for col in range(4):
                rectangles[row].append(self.addRect(QRectF(0, 0, 115, 115), QColor(85,84,90,50), QColor(85,84,90,50)))
                texts[row].append(self.addText("5", font))
                rectangles[row][col].setPos(120 * col + 12.5, 120 * row + 90)
                texts[row][col].setPos(120 * col + 50, 120 * row + 117)  

        print(rectangles[0][0].scenePos())
        print(rectangles[0][0].pos())



