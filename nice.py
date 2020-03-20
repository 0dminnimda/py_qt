import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
import PyQt5


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.wid = 150
        self.hig = 150

        self.setWindowTitle('Example') # имя окна
        self.setGeometry(200, 200, self.wid, self.hig) # рамки
        self.setAttribute(Qt.WA_TranslucentBackground, True) # прозрачные внутренности окна
        self.setWindowFlags(Qt.FramelessWindowHint) # без сноски с именем окна

        self.press = False # нажато ли окно
        self.last_pos = QPoint(0, 0) # window pos

    def mouseMoveEvent(self, event):
        if self.press:
            self.move(event.globalPos() - self.last_pos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.press = True

        self.last_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.press = False

    def paintEvent(self, event: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        size = 25
        painter.setPen(QtGui.QPen(Qt.green, size)) # настройки "кисти"
        painter.drawEllipse(
            PyQt5.QtCore.QPoint(self.wid//2, self.hig//2),
            self.wid/2-size/2, self.hig/2-size/2) # форма окна
        #print(self.rect().width())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Example()
    w.show()

    sys.exit(app.exec_())