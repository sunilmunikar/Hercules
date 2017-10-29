# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\devPythonLocus\ui_mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFormLayout

import Locus_entry_ui
import form_layout_ui
from locus_data import LocusDataEntryDialog
from locusDetailed import *

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

        '''Home Button'''
        self.Home = QtGui.QToolButton(self.frame)
        self.Home.setGeometry(QtCore.QRect(0, 0, 121, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
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
        self.Home.setCheckable(True)
        self.Home.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.Home.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Home.setObjectName(_fromUtf8("Home"))

        '''Data Entry Button '''
        self.DataEntry = QtGui.QToolButton(self.frame)
        self.DataEntry.setGeometry(QtCore.QRect(0, 60, 121, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
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

        self.Locus = QtGui.QToolButton(self.frame)
        self.Locus.setGeometry(QtCore.QRect(20, 110, 100, 40))
        self.Locus.setCheckable(True)
        self.Locus.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.Locus.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.Locus.setObjectName(_fromUtf8("Locus"))

        self.find = QtGui.QToolButton(self.frame)
        self.find.setGeometry(QtCore.QRect(20, 150, 100, 40))
        self.find.setCheckable(True)
        self.find.setObjectName(_fromUtf8("find"))

        self.sample = QtGui.QToolButton(self.frame)
        self.sample.setGeometry(QtCore.QRect(20, 190, 100, 40))
        self.sample.setCheckable(True)
        self.sample.setObjectName(_fromUtf8("sample"))






        '''stacked widget settings'''

        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(130, 0, 600, 700))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.stackedWidget.setSizePolicy(sizePolicy)

        '''homepage layout settings '''
        #set the background color800

        homepageWidget = QtGui.QWidget()
        homepageWidget.setAutoFillBackground(True)
        p = homepageWidget.palette()
        p.setColor(homepageWidget.backgroundRole(), QtCore.Qt.lightGray)
        homepageWidget.setPalette(p)



        self.Homepage = homepageWidget

        layout_homepage = QFormLayout()

        layout_homepage.setGeometry(QtCore.QRect(130, 0, 300, 591))
        layout_homepage.addRow("Project Title", QtGui.QLineEdit())
        layout_homepage.addRow("Project Type", QtGui.QLabel())

        layout_homepage.addWidget(QtGui.QCheckBox("Archeological Project"))
        layout_homepage.addWidget(QtGui.QComboBox())

        layout_homepage.addWidget(QtGui.QCheckBox("Fieldwork Activity"))
        layout_homepage.addWidget(QtGui.QComboBox())

        horizontalSpacer = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout_homepage.addItem(horizontalSpacer)

        sl_value = QtGui.QSlider()
        # sl_value.setGeometry(QtCore.QRect(0, 0, 0, 0))
        sl_value.setOrientation(QtCore.Qt.Horizontal)
        sl_value.setObjectName("sl_value")
        layout_homepage.addWidget(sl_value)

        horizontalSpacer1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout_homepage.addItem(horizontalSpacer1)

        site = QtGui.QLineEdit()
        site.setFixedWidth(200)
        layout_homepage.addRow("Site", site)

        horizontalSpacer1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout_homepage.addItem(horizontalSpacer1)

        date = QtGui.QLineEdit()
        date.setFixedWidth(200)
        layout_homepage.addRow("Date", date)

        horizontalSpacer2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout_homepage.addItem(horizontalSpacer2)

        studyArea = QtGui.QLineEdit()
        studyArea.setFixedWidth(200)
        layout_homepage.addRow("Study Area", studyArea)

        horizontalSpacer3 = QtGui.QSpacerItem(40, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout_homepage.addItem(horizontalSpacer3)

        saveproject = QtGui.QPushButton()
        saveproject.setText("Save Project")
        saveproject.setFixedWidth(150)
        layout_homepage.addWidget(saveproject)



       # layout.addRow("Study Area", QtGui.QLineEdit())

        self.Homepage.setLayout(layout_homepage)

        self.Homepage.setObjectName(_fromUtf8("Homepage"))
        self.stackedWidget.addWidget(self.Homepage)

        ###''' data entry toolbar '''

        self.DataEntrypage = QtGui.QWidget()
        layout_dataentry = QFormLayout()
        verticalSpacer = QtGui.QSpacerItem(40, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout_dataentry.addItem(verticalSpacer)



        # layout_dataentry.addRow("ADD NEW", QtGui.QLabel())
        # verticalSpacer = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        # layout_dataentry.addItem(verticalSpacer)

       #
       #  """Add locus buttton"""
       #  locusButton = QtGui.QPushButton()
       #  locusButton.setText("LOCUS")
       #  locusButton.setStyleSheet("background-color: grey; color: white ;")
       # # locusButton.setFixedHeight(30)
       #  locusButton.setFixedWidth(130)
       #
       #  #locusButton.setGeometry(140,80,75,23)
       #  #locusButton.setGeometry(QtCore.QRect(QtCore.QPoint(300,200),QtCore.QSize(400,430)))
       #  #locusButton.move(300, 140)
       #  layout_dataentry.addWidget(locusButton)
       #  self.connect(locusButton, QtCore.SIGNAL('clicked()'), self.locusentry)
       #
       # # locusButton.clicked.connect(self.locusentry)
       #
       #
       #
       #  """Add find button """
       #
       #  findButton = QtGui.QPushButton()
       #  findButton.setText("FIND")
       #  findButton.setStyleSheet("background-color: grey; color: white ;")
       #  # locusButton.setFixedHeight(30)
       #  findButton.setFixedWidth(130)
       #  # locusButton.setGeometry(140,80,75,23)
       #  # locusButton.setGeometry(QtCore.QRect(QtCore.QPoint(300,200),QtCore.QSize(400,430)))
       #  # locusButton.move(300, 140)
       #  layout_dataentry.addWidget(findButton)
       #
       #  """Add Sample """
       #  SampleButton = QtGui.QPushButton()
       #  SampleButton.setText("SAMPLE")
       #  SampleButton.setStyleSheet("background-color: grey; color: white ;")
       #  # locusButton.setFixedHeight(30)
       #  SampleButton.setFixedWidth(130)
       #  # locusButton.setGeometry(140,80,75,23)
       #  # locusButton.setGeometry(QtCore.QRect(QtCore.QPoint(300,200),QtCore.QSize(400,430)))
       #  # locusButton.move(300, 140)
       #  layout_dataentry.addWidget(SampleButton)






        #
        # homepageWidget.setAutoFillBackground(True)
        # p = homepageWidget.palette()
        # p.setColor(homepageWidget.backgroundRole(), QtCore.Qt.lightGray)
        # homepageWidget.setPalette(p)



        # self.DataEntryLayout = QFormLayout()
        # self.DataEntryLayout.addWidget(QtGui.QToolButton())
        #
        # self.DataEntryLayout.addRow("acheckbox", QtGui.QCheckBox())

        """""""#set the layout"""
        self.DataEntrypage.setLayout(layout_dataentry)
        self.DataEntrypage.setObjectName(_fromUtf8("DataEntrypage"))
        self.stackedWidget.addWidget(self.DataEntrypage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        '''locus widget'''

        #locuspageWidget = QtGui.QWidget()
        locuspageWidget = LocusDetailedDialog()



        locuspageWidget.setAutoFillBackground(True)
        p = locuspageWidget.palette()
        p.setColor(locuspageWidget.backgroundRole(), QtCore.Qt.lightGray)
        locuspageWidget.setPalette(p)

        self.Locuspage = locuspageWidget

        #layout_locuspage = QFormLayout()
        #layout_locuspage.addRow("Project Title", QtGui.QLineEdit())

        #layout_homepage.setGeometry(QtCore.QRect(130, 0, 300, 591))


        self.locuspage = locuspageWidget
        #self.locuspage.show()
        #self.Locuspage.setLayout(layout_locuspage)

        self.Locuspage.setObjectName(_fromUtf8("Locuspage"))

        self.stackedWidget.addWidget(self.Locuspage)




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ArcheoHerculesMap: DataCollection", None))
        self.Home.setText(_translate("MainWindow", "Home", None))
        self.DataEntry.setText(_translate("MainWindow", "Data Entry", None))
        self.Locus.setText(_translate("MainWindow", "LOCUS", None))
        self.find.setText(_translate("MainWindow", "FIND", None))
        self.sample.setText(_translate("MainWindow", "SAMPLE", None))




    def locusentry(self):

        #locus = Locus_entry_ui.Ui_Form()
        #locus.Save()
        #locus.show()
        locusshow = LocusDataEntryDialog(self)
        locusshow.show()
        #print "test"

