# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\devPythonLocus\ui_mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 123, 648))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.Home = QtGui.QToolButton(self.frame)
        self.Home.setGeometry(QtCore.QRect(0, 0, 121, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Home.sizePolicy().hasHeightForWidth())
        self.Home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Home.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/home")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home.setIcon(icon)
        self.Home.setIconSize(QtCore.QSize(48, 48))
        self.Home.setCheckable(False)
        self.Home.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.Home.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Home.setObjectName(_fromUtf8("Home"))
        self.DataEntry = QtGui.QToolButton(self.frame)
        self.DataEntry.setGeometry(QtCore.QRect(0, 60, 121, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataEntry.sizePolicy().hasHeightForWidth())
        self.DataEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.DataEntry.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/dataentry")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DataEntry.setIcon(icon1)
        self.DataEntry.setIconSize(QtCore.QSize(48, 48))
        self.DataEntry.setCheckable(False)
        self.DataEntry.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.DataEntry.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.DataEntry.setObjectName(_fromUtf8("DataEntry"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ArcheoHerculesMap: DataCollection", None))
        self.Home.setText(_translate("MainWindow", "Home", None))
        self.DataEntry.setText(_translate("MainWindow", "Data Entry", None))

import resources_rc
