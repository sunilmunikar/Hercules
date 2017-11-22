# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'locus.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import UpdateDeleteWidget


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
        Form.resize(530, 633)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_1 = QtGui.QHBoxLayout()

        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))

        self.LocusIdLabel = QtGui.QLabel(Form)
        self.LocusIdLabel.setObjectName(_fromUtf8("LocusIdLabel"))
        self.horizontalLayout_1.addWidget(self.LocusIdLabel)

        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.LocusIdEntry = QtGui.QLineEdit(Form)
        self.LocusIdEntry.setObjectName(_fromUtf8("LocusIdEntry"))
        self.verticalLayout.addWidget(self.LocusIdEntry)

        self.LocusTypeLabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LocusTypeLabel.setFont(font)
        self.LocusTypeLabel.setObjectName(_fromUtf8("LocusTypeLabel"))
        self.verticalLayout.addWidget(self.LocusTypeLabel)
        self.LocusTypeEntry = QtGui.QComboBox(Form)
        font = QtGui.QFont()
        #font.setItalic(True)
        self.LocusTypeEntry.setFont(font)
        self.LocusTypeEntry.setMouseTracking(True)
        self.LocusTypeEntry.setInputMethodHints(QtCore.Qt.ImhNone)
        self.LocusTypeEntry.addItems([
            "CONCENTRATION",
            "CORING",
            "DOOR",
            "FEATURE",
            "FLOOR",
            "FREESTANDING MONUMENT",
            "HEATING INFRASTRUCTURE",
            "INTERFACE",
            "LAYER",
            "LENZING",
            "MAPPING",
            "OBJECT",
            "OBSERVATION",
            "PROFILE",
            "STAIR",
            "SUPERSTRUCTURE",
            "VERTICAL ELEVATION",
            "WATER INFRASTRUCTURE",
            "WINDOW",
            "HORIZONTAL ELEVATION"])

        self.LocusTypeEntry.setObjectName(_fromUtf8("LocusTypeEntry"))
        self.verticalLayout.addWidget(self.LocusTypeEntry)

        self.SectorTrenchLabel = QtGui.QLabel(Form)
        self.SectorTrenchLabel.setObjectName(_fromUtf8("SectorTrenchLabel"))
        self.verticalLayout.addWidget(self.SectorTrenchLabel)
        self.SectorTrenchEntry = QtGui.QLineEdit(Form)
        self.SectorTrenchEntry.setObjectName(_fromUtf8("SectorTrenchEntry"))
        self.verticalLayout.addWidget(self.SectorTrenchEntry)

        self.SpaceRoomLabel = QtGui.QLabel(Form)
        self.SpaceRoomLabel.setObjectName(_fromUtf8("SpaceRoomLabel"))
        self.verticalLayout.addWidget(self.SpaceRoomLabel)
        self.SpaceRoomEntry = QtGui.QLineEdit(Form)
        self.SpaceRoomEntry.setObjectName(_fromUtf8("SpaceRoomEntry"))
        self.verticalLayout.addWidget(self.SpaceRoomEntry)

        self.DescriptionLabel = QtGui.QLabel(Form)
        self.DescriptionLabel.setObjectName(_fromUtf8("DescriptionLabel"))
        self.verticalLayout.addWidget(self.DescriptionLabel)
        self.DescriptionEntry = QtGui.QPlainTextEdit(Form)
        self.DescriptionEntry.setStyleSheet(_fromUtf8("font: 10pt \"Arial Narrow\";"))
        self.DescriptionEntry.setObjectName(_fromUtf8("DescriptionEntry"))
        self.verticalLayout.addWidget(self.DescriptionEntry)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

      # """buttons in the form"""

        self.Save = QtGui.QPushButton(Form)
        self.Save.setObjectName(_fromUtf8("Save"))
        self.horizontalLayout.addWidget(self.Save)
        self.Update = QtGui.QPushButton(Form)
        self.Update.setObjectName(_fromUtf8("Update"))
        self.horizontalLayout.addWidget(self.Update)
        self.Close = QtGui.QPushButton(Form)
        self.Close.setObjectName(_fromUtf8("Close"))
        self.horizontalLayout.addWidget(self.Close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ShowAll = QtGui.QPushButton(Form)
        self.ShowAll.setMaximumSize(QtCore.QSize(16777215, 16777197))
        self.ShowAll.setObjectName(_fromUtf8("ShowAll"))
        self.verticalLayout.addWidget(self.ShowAll)

      # """set buddy of the form"""
        self.LocusIdLabel.setBuddy(self.SpaceRoomEntry)
        self.LocusTypeLabel.setBuddy(self.LocusTypeEntry)
        self.SectorTrenchLabel.setBuddy(self.SpaceRoomEntry)
        self.SpaceRoomLabel.setBuddy(self.SpaceRoomEntry)
        self.DescriptionLabel.setBuddy(self.DescriptionEntry)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.LocusTypeEntry, self.SpaceRoomEntry)
        Form.setTabOrder(self.SpaceRoomEntry, self.DescriptionEntry)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.LocusIdLabel.setText(_translate("Form", "Locus ID", None))
        self.LocusTypeLabel.setText(_translate("Form", "Locus Type", None))
        self.SectorTrenchLabel.setText(_translate("Form", "Sector/Trench", None))
        self.SpaceRoomLabel.setText(_translate("Form", "Space room", None))
        self.DescriptionLabel.setText(_translate("Form", "Description", None))
        self.Save.setText(_translate("Form", "Save", None))
        self.Update.setText(_translate("Form", "Update", None))
        self.Close.setText(_translate("Form", "Close", None))
        self.ShowAll.setText(_translate("Form", "Show All", None))


#
# UpdateDeleteTab = UpdateDeleteWidget.UpdateDelete()
# tabs = qt.QTabWidget()
# tabs.addTab(UpdateDeleteTab, "Update/Delete")
# tabs.setGeometry(450, 100, 400, 520)
# tabs.setWindowTitle('CoinTableEdit')
# tabs.show()
