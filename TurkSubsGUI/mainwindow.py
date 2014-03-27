# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workspace\TurkSubs\mainwindow.ui'
#
# Created: Wed Mar 26 21:41:03 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(574, 370)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.userString = QtGui.QLabel(self.centralwidget)
        self.userString.setGeometry(QtCore.QRect(0, 0, 231, 20))
        self.userString.setObjectName(_fromUtf8("userString"))
        self.urlField = QtGui.QLineEdit(self.centralwidget)
        self.urlField.setGeometry(QtCore.QRect(192, 40, 211, 20))
        self.urlField.setAlignment(QtCore.Qt.AlignCenter)
        self.urlField.setObjectName(_fromUtf8("urlField"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 111, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 70, 111, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.videoLengthField = QtGui.QLineEdit(self.centralwidget)
        self.videoLengthField.setGeometry(QtCore.QRect(240, 90, 113, 20))
        self.videoLengthField.setAlignment(QtCore.Qt.AlignCenter)
        self.videoLengthField.setObjectName(_fromUtf8("videoLengthField"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 120, 111, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.splitLengthField = QtGui.QLineEdit(self.centralwidget)
        self.splitLengthField.setGeometry(QtCore.QRect(240, 140, 113, 20))
        self.splitLengthField.setAlignment(QtCore.Qt.AlignCenter)
        self.splitLengthField.setObjectName(_fromUtf8("splitLengthField"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 170, 111, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.salaryField = QtGui.QLineEdit(self.centralwidget)
        self.salaryField.setGeometry(QtCore.QRect(240, 190, 113, 20))
        self.salaryField.setAlignment(QtCore.Qt.AlignCenter)
        self.salaryField.setObjectName(_fromUtf8("salaryField"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 220, 111, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.numOfTurkersField = QtGui.QLineEdit(self.centralwidget)
        self.numOfTurkersField.setGeometry(QtCore.QRect(240, 240, 113, 20))
        self.numOfTurkersField.setAlignment(QtCore.Qt.AlignCenter)
        self.numOfTurkersField.setObjectName(_fromUtf8("numOfTurkersField"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 290, 111, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 90, 81, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 140, 81, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 190, 81, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(350, 240, 91, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Form1", None))
        self.userString.setText(_translate("MainWindow", "User: NULL", None))
        self.label.setText(_translate("MainWindow", "Youtube URL", None))
        self.label_2.setText(_translate("MainWindow", "Length of Video", None))
        self.label_3.setText(_translate("MainWindow", "Length of Splits", None))
        self.splitLengthField.setText(_translate("MainWindow", "10", None))
        self.label_4.setText(_translate("MainWindow", "Turker Salary", None))
        self.salaryField.setText(_translate("MainWindow", "0.05", None))
        self.label_5.setText(_translate("MainWindow", "Number of Turkers", None))
        self.numOfTurkersField.setText(_translate("MainWindow", "5", None))
        self.pushButton.setText(_translate("MainWindow", "Submit", None))
        self.label_6.setText(_translate("MainWindow", "hh:mm:ss", None))
        self.label_7.setText(_translate("MainWindow", "seconds", None))
        self.label_8.setText(_translate("MainWindow", "dollars", None))
        self.label_9.setText(_translate("MainWindow", "natural number", None))

class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
