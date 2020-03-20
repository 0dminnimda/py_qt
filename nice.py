# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtGui
import PyQt5

from PyQt5.QtWidgets import QDesktopWidget,QApplication


class Example(QWidget):
    def __init__(self, win_wid=0, win_hei=0):
        super().__init__()

        self.text = "asdasdas"

        self.wid = self.hig = 150

        shape = [200, 200, self.wid, self.hig]

        self.setWindowTitle('Example') # имя окна
        self.setGeometry(*shape) # рамки
        self.setAttribute(Qt.WA_TranslucentBackground, True) # прозрачные внутренности окна
        self.setWindowFlags(Qt.FramelessWindowHint) # без сноски с именем окна

        self.press = False # нажато ли окно
        self.last_pos = QPoint(0, 0) # window pos

    def drawText(self, event, qp):

        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 15))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

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
        size = 7
        pos = PyQt5.QtCore.QPoint(self.wid//2, self.hig//2)
        painter.setPen(QtGui.QPen(Qt.black, size)) # настройки "кисти"
        painter.drawEllipse(pos, self.wid/2-size, self.hig/2-size) # форма окна

        painter.setPen(QtGui.QPen(Qt.white, size)) # настройки "кисти"
        painter.drawEllipse(pos, self.wid/2-size*2, self.hig/2-size*2) # форма окна

        self.drawText(event, painter)

class Draw(QWidget):
    def __init__(self, win_wid=0, win_hei=0):
        super().__init__()

        self.wid = self.hig = 150

        shape = [200, 200, self.wid, self.hig]

        col = QColor(200, 0, 0)
        QColor.setAlpha(col, 100)

        #p = self.palette()
        #p.setColor(self.backgroundRole(), col) #
        #self.setPalette(p)

        self.setWindowTitle('Example') # имя окна
        self.setGeometry(*shape) # рамки
        self.set_transparency(not False)

        #self.setAutoFillBackground(False)
        #self.setAttribute(Qt.WA_NoSystemBackground, False)
        #self.setAttribute(Qt.WA_TranslucentBackground, True) # прозрачные внутренности окна
        self.setWindowFlags(Qt.FramelessWindowHint) # без сноски с именем окна

        self.press = False # нажато ли окно
        self.last_pos = QPoint(0, 0) # window pos

    def set_transparency(self, enabled):
        if enabled:
            self.setAutoFillBackground(not False)
        else:
            self.setAttribute(Qt.WA_NoSystemBackground, False)

        self.setAttribute(Qt.WA_TranslucentBackground, enabled)
        self.repaint()


    def mouseMoveEvent(self, event):
        if self.press:
            self.move(event.globalPos() - self.last_pos)
        #print("gg")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.press = True
        print("df")

        self.last_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.press = False

    def paintEvent(self, event: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        size = 50
        #pos = PyQt5.QtCore.QPoint(self.wid//2, self.hig//2)
        painter.setPen(QtGui.QPen(Qt.white, size)) # настройки "кисти"
        painter.drawRect(self.rect())#, self.wid/2-size, self.hig/2-size) # форма окна

if __name__ == '__main__':
    app = QApplication(sys.argv)
    q = QDesktopWidget().availableGeometry()
    wid = q.width()
    hei = q.height()
    #print(f"{wid=}")
    #print(f"{hei=}")

    #app = QApplication(sys.argv)

    wind = Draw()
    #print(Example)
    wind.show()

    sys.exit(app.exec_())