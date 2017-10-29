# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\devPythonLocus\form_layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(820, 647)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(170, 230, 385, 79))
        self.frame.setStyleSheet(_fromUtf8("QFrame{\n"
"boder-bottom: 3px solid darkgrey;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(163, 167, 218, 158), stop:0.903409 rgba(255, 255, 255, 255));\n"
"}\n"
"QToolButton{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(218, 168, 163, 158), stop:0.903409 rgba(255, 255, 255, 255));\n"
"    font: 75 11pt \"MS Sans Serif\";\n"
"    border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), "
"stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), "
                                           "stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"    \n"
"    border-color: rgb(0, 170, 0);\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.toolButton = QtGui.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(24, 18, 71, 41))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(280, 20, 81, 41))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(150, 20, 81, 41))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 170, 78, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayoutWidget = QtGui.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 80, 701, 501))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.comboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.toolButton.setText(_translate("Form", "Locus", None))
        self.toolButton_2.setText(_translate("Form", "Sample", None))
        self.toolButton_3.setText(_translate("Form", "Find", None))
        self.label.setText(_translate("Form", "Add New", None))

