# window.py

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QIcon, QColor, QFont, QFontMetrics
from PyQt6.QtCore import  QSize, Qt, QRect, QRectF, QPointF

font = QFont("Clear Sans", 35, QFont.Weight.Bold)
class GraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setBackgroundBrush(QColor(255,240,232,255))
        self.setSceneRect(0, 0, 550, 630) # Set the scene rectangle size
        rectangles = []
        texts = []
        title_text = self.addSimpleText("2048", QFont("Clear Sans", 50, QFont.Weight.Bold))
        title_text.setPos(10, 2)
        title_text.setBrush(QColor(119,110,101,255))
        signature = self.addSimpleText("Created by: Emmanuel Pierre", QFont("Clear Sans", 16))
        signature.setPos(335, 605)
        self.addRect(QRectF(0, 0, 520, 540), QColor(187,173,160,255), QColor(187,173,160,255)).setPos(14, 62)
        font_metrics = QFontMetrics(font)

        for row in range(4):
            rectangles.append([])
            texts.append([])
            for col in range(4):
                text = "2" if row == 0 and col == 0 else ""
                text_width = font_metrics.horizontalAdvance(text)  # Get the width of the text
                text_height = font_metrics.height() 
                rectangles[row].append(self.addRect(QRectF(0, 0, 115, 115), QColor(228,221,214,70), QColor(228,221,214,70)))
                texts[row].append(self.addSimpleText(text, font))
                rectangles[row][col].setPos(130 * col + 21.5, 130 * row + 80)
                texts[row][col].setPos(rectangles[row][col].x() + 115 / 2 - text_width / 2, rectangles[row][col].y() + 115 / 2 - text_height / 2)
                texts[row][col].setBrush(QColor(119,110,101,255))

        rectangles[0][0].setBrush(QColor(238,228,218,255))
        print(rectangles[0][0].scenePos())
        print(rectangles[0][0].pos())



