# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup_test_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.popup = QtWidgets.QPushButton(self.centralwidget)
        self.popup.setGeometry(QtCore.QRect(180, 170, 401, 161))
        self.popup.setObjectName("popup")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #notice no parentheses on the end of the function name e.g. show_popup
        self.popup.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.popup.setText(_translate("MainWindow", "Popup"))


    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("This is the window title")
        msg.setText("This is the main text!")

        # warning, critical, question, information = 4 types of icons available
        msg.setIcon(QMessageBox.Warning)

        # sets the buttons that will appear inside the popup window
        '''
            full list:  https://doc.qt.io/qt-5/qmessagebox.html
            QMessageBox.Ok
            QMessageBox.Open
            QMessageBox.Save
            QMessageBox.Cancel
            QMessageBox.Close
            QMessageBox.Discard
            QMessageBox.Apply
            QMessageBox.Reset
            QMessageBox.Help
            QMessageBox.RestoreDefaults
            QMessageBox.Yes
            QMessageBox.No
            QMessageBox.Abort
            QMessageBox.Retry
            QMessageBox.Ignore
        '''
        msg.setStandardButtons( QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel )
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setInformativeText("some informative text for you")

        msg.setDetailedText("some details for you")

        msg.buttonClicked.connect(self.popup_button)

        # What actually shows the message box
        x = msg.exec_()

    def popup_button(self, i):
        print(i.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
