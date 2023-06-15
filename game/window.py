# window.py
from twenty48 import Twenty48 as t48
import math
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QIcon, QColor, QFont, QFontMetrics, QKeyEvent
from PyQt6.QtCore import  QSize, Qt, QRect, QRectF, QPointF, QEvent

font_name = ""
font = QFont(font_name, 35, QFont.Weight.Bold)
class GraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setBackgroundBrush(QColor(255,240,232,255))
        self.setSceneRect(0, 0, 550, 630) # Set the scene rectangle size
        self.rectangles = []
        self.texts = []
        self.title_text = self.addSimpleText("2048", QFont("", 50, QFont.Weight.Bold))
        self.title_text.setPos(10, 2)
        self.title_text.setBrush(QColor(119,110,101,255))
        self.signature = self.addSimpleText("Created by: Emmanuel Pierre", QFont(font_name, 16))
        self.signature.setPos(335, 605)
        self.addRect(QRectF(0, 0, 520, 540), QColor(187,173,160,255), QColor(187,173,160,255)).setPos(14, 62)
        self.font_metrics = QFontMetrics(font)
        self.game = t48()
        self.game.board[random.randint(0,3)][random.randint(0,3)] = 2

        for row in range(4):
            self.rectangles.append([])
            self.texts.append([])
            for col in range(4):
                text = ""
                text_width = self.font_metrics.horizontalAdvance(text)  # Get the width of the text
                text_height = self.font_metrics.height() 
                self.rectangles[row].append(self.addRect(QRectF(0, 0, 115, 115), QColor(228,221,214,70), QColor(228,221,214,70)))
                self.texts[row].append(self.addSimpleText(text, font))
                self.rectangles[row][col].setPos(130 * col + 21.5, 130 * row + 80)
                self.texts[row][col].setPos(self.rectangles[row][col].x() + 115 / 2 - text_width / 2, self.rectangles[row][col].y() + 115 / 2 - text_height / 2)
                self.texts[row][col].setBrush(QColor(119,110,101,255))
        self.updateboard()

    def updateboard(self):
        for row in range(4):
            for col in range(4):
                num = self.game.board[row][col]
                text = str(self.game.board[row][col])
                if text == "0":
                    text = ""
                text_width = self.font_metrics.horizontalAdvance(text)  # Get the width of the text
                text_height = self.font_metrics.height() 
                self.texts[row][col].setText(text)
                self.texts[row][col].setPos(self.rectangles[row][col].x() + 115 / 2 - text_width / 2, self.rectangles[row][col].y() + 115 / 2 - text_height / 2)
                if num > 0: self.rectangles[row][col].setBrush(QColor(180, 150 + int((math.log(2, num) * 10)), 150 + int((math.log(2,num) * 10)), 255))
                if num == 0: self.rectangles[row][col].setBrush(QColor(228,221,214,70))
        

    def keyPressEvent(self, event: QKeyEvent) -> None:
        valid_keys = [Qt.Key.Key_Up, Qt.Key.Key_Down, Qt.Key.Key_Left, Qt.Key.Key_Right]
        if event.key() == Qt.Key.Key_Up:
            self.game.push("Up")
        elif event.key() == Qt.Key.Key_Down:
            self.game.push("Down")
        elif event.key() == Qt.Key.Key_Left:
            self.game.push("Left")
        elif event.key() == Qt.Key.Key_Right:
            self.game.push("Right")
        if event.key() in valid_keys:
            self.setRandomIndex()
            self.updateboard()

    def setRandomIndex(self):
        random_x = random.randint(0,3)
        random_y = random.randint(0,3)
        if self.game.board[random_x][random_y] != 0:
            self.setRandomIndex()
        else:
            self.game.board[random_x][random_y] = 2



