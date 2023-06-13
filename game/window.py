# window.py

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import  QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game 2048")
        self.setWindowIcon(QIcon("/Game_2048/resources/2048_logo.png"))
        self.setFixedSize(500,500)
