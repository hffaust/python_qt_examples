from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):

    # ensure that the parent constructor is called
    def __init__(self):
        super(MyWindow, self).__init__()
        # set size of window
        # xpos, ypos is where you want the window to show up
        #  corresponds to the position of the top left hand corner
        xpos = 200
        ypos = 200
        width = 300
        height = 300
        self.setGeometry(xpos, ypos, width, height)
        # set title of window
        self.setWindowTitle("Main Window")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label")
        self.label.move(50, 50)

        # adding buttons
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)


    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()

    sys.exit(app.exec_())

window()
