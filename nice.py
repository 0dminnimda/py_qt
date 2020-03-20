# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtGui
import PyQt5


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.wid = 150
        self.hig = 150

        self.setWindowTitle('Example') # имя окна
        self.setGeometry(200, 200, self.wid, self.hig) # рамки
        self.setAttribute(Qt.WA_TranslucentBackground, True) # прозрачные внутренности окна
        self.setWindowFlags(Qt.FramelessWindowHint) # без сноски с именем окна

        self.press = False # нажато ли окно
        self.last_pos = QPoint(0, 0) # window pos

    def initUI(self):

        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'



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
        #print(self.pos())

        #qp = QPainter()
        #qp.begin(self)
        self.drawText(event, painter)
        #qp.end()

class mywindow(QMainWindow):
 
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Example()
        self.ui.setupUi(self)
        
        self.ui.label.setFont(
            QtGui.QFont('SansSerif', 30)
        )
 
        self.ui.label.setGeometry(
            QtCore.QRect(0, 0, 50, 50)
        ) # изменить геометрию ярлыка'''


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wind = Example()
    #print(Example)
    wind.show()

    sys.exit(app.exec_())