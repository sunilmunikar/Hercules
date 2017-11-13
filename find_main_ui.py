import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection



class FindMainDialog(QtGui.QTabWidget):
    def __init__(self):
        super(FindMainDialog, self).__init__()

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.lightGray)
        self.setPalette(p)

        self.tab1 = QtGui.QWidget()
        self.tab2 = QtGui.QWidget()
        self.tab3 = QtGui.QWidget()
        self.tab4 = QtGui.QWidget()
        self.tab5 = QtGui.QWidget()
        self.tab6 = QtGui.QWidget()
        self.tab7 = QtGui.QWidget()



        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")
        self.addTab(self.tab5, "Tab 5")
        self.addTab(self.tab6, "Tab 6")
        self.addTab(self.tab7, "Tab 7")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()
        self.tab7UI()


    def tab1UI(self):
        self.gridlayout = QtGui.QGridLayout()
        #self.gridlayout.setHorizontalSpacing(0)

        self.FindID = QtGui.QLineEdit()
        #self.FindID.setFixedWidth(150)

        self.LocusID = QtGui.QLineEdit()
        #self.LocusID.setFixedWidth(150)



        self.MaterialCategory = QtGui.QComboBox()
        #self.MaterialCategory.setFixedWidth(150)

        # self.Chronology = QtGui.QPushButton('Chronology', self)
        # # self.Floor.setStyleSheet("QtGui.QPushButton { background-color: blue}")
        # self.Chronology.setStyleSheet(
        #     'QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
        #     ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
        #     'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')
        #
        # self.Coin = QtGui.QPushButton('Coin', self)
        # self.Coin.setStyleSheet(
        #     'QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
        #     ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
        #     'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')
        #
        # self.FindImport = QtGui.QPushButton('Find Import', self)
        # self.FindImport.setStyleSheet(
        #     'QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
        #     ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
        #     'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')
        #
        # self.Glass = QtGui.QPushButton('Glass', self)
        # self.Glass.setStyleSheet(
        #     'QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
        #     ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
        #     'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')
        #
        # self.MetalObject = QtGui.QPushButton('Metal Object', self)
        # self.MetalObject.setStyleSheet(
        #     'QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
        #     ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
        #     'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')

        # self.WorkedBone = QtGui.QPushButton('Worked Bone', self)
        # self.WorkedBone.setStyleSheet(
        #     'QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
        #     ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
        #     'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')




        self.SaveFind = QtGui.QPushButton()
        self.SaveFind.setText("Save Project")
        self.SaveFind.setFixedWidth(150)
        #selayout_homepage.addWidget(saveproject)

        self.Map = QtGui.QPushButton('Map')

        self.gridlayout.addWidget(QtGui.QLabel('Find ID: ', self), 1, 0)
        self.gridlayout.addWidget(self.FindID, 1, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Context Locus ID: ', self), 2, 0)
        self.gridlayout.addWidget(self.LocusID, 2, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Material Category: ', self), 3, 0)
        self.gridlayout.addWidget(self.MaterialCategory, 3, 1, 1, 1)
        self.gridlayout.setRowStretch(4, 1)
        self.gridlayout.setRowStretch(8, 1)

        self.gridlayout.addWidget(self.Map, 9, 0)
        self.gridlayout.addWidget(self.SaveFind, 9, 1)



        #
        # self.gridlayout.addWidget(self.Chronology, 5, 1, 1, 1)
        # self.gridlayout.addWidget(self.Coin, 5, 2, 1, 1)
        # self.gridlayout.addWidget(self.FindImport, 5, 3, 1, 1)
        # self.gridlayout.addWidget(self.Glass, 7, 1, 1, 1)
        # self.gridlayout.addWidget(self.MetalObject, 7, 2, 1, 1)
        # self.gridlayout.addWidget(self.WorkedBone, 7, 3, 1, 1)




        # self.gridlayout.addWidget(self.LocusIDBox, 4, 3)
        #
        #
        #
        # self.gridlayout.addWidget(self.ProjectName, 6, 1)
        # self.ProjectName.setPlaceholderText('Search the project Name')
        # self.LocusID.setPlaceholderText('Search the Locus Id')

        #
        # self.gridlayout.addWidget(self.LocusID, 6, 3)


        #self.gridlayout.addWidget(self.saveproject, 11, 2)
        #self.gridlayout.addWidget(QtGui.QLabel('', self), 12, 0)
        self.gridlayout.setRowStretch(13, 1)
        self.gridlayout.setColumnStretch(4, 1)

        #self.gridlayout.setColumnMinimumWidth(2, 3)

        self.setLayout(self.gridlayout)
        self.resize(300, 200)

        '''set tab name '''
        self.setTabText(0, "Find")
        self.tab1.setLayout(self.gridlayout)

        #self.setWindowTitle('Add New Project')

    def tab2UI(self):
        '''set tab name '''
        self.setTabText(1, "Chronology")
        #self.tab2.setLayout(self.tab2layout)

    def tab3UI(self):
        '''set tab name '''
        self.setTabText(2, "Coin")
        #self.tab2.setLayout(self.tab2layout)

    def tab4UI(self):
        '''set tab name '''
        self.setTabText(3, "Find Import")
        #self.tab2.setLayout(self.tab2layout)

    def tab5UI(self):
        '''set tab name '''
        self.setTabText(4, "Glass")
        #self.tab2.setLayout(self.tab2layout)

    def tab6UI(self):
        '''set tab name '''
        self.setTabText(5, "Metal Object")
        #self.tab2.setLayout(self.tab2layout)

    def tab7UI(self):
        '''set tab name '''
        self.setTabText(6, "Worked Bone")
        # self.tab2.setLayout(self.tab2layout)

























