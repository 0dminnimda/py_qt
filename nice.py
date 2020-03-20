import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Example') # имя окна
        self.setGeometry(50, 50, 500, 500) # рамки
        self.setAttribute(Qt.WA_TranslucentBackground, True) # прозрачные внутренности окна
        self.setWindowFlags(Qt.FramelessWindowHint) # без сноски с именем окна

        self.press = False # ?
        self.last_pos = QPoint(0, 0) # ?

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
        painter.setPen(QtGui.QPen(Qt.green, 100))
        painter.drawRect(self.rect())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Example()
    w.show()

    sys.exit(app.exec_())