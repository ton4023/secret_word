import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "BLACKPINK Secret Word Song"
        self.left = 200
        self.top = 200
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(30, 30)
        self.textbox1.resize(280, 40)

        self.button = QPushButton('Click me', self)
        self.button.move(15, 85)
        self.button.clicked.connect(self.on_click)
        self.show()

    pyqtSlot()

    def on_click(self):
        textboxValue = self.textbox1.text()
        QMessageBox.question(self, 'Hello', 'Confirm: ' + textboxValue, QMessageBox.Ok,  QMessageBox.Cancel)
        self.textbox1.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
