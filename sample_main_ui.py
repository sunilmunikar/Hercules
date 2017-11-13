import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection


class SampleMainDialog(QtGui.QTabWidget):
    def __init__(self):
        super(SampleMainDialog, self).__init__()

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.lightGray)
        self.setPalette(p)

        self.tab1 = QtGui.QWidget()
        self.tab2 = QtGui.QWidget()


        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")


        self.tab1UI()
        self.tab2UI()

    def tab1UI(self):
        self.gridlayout = QtGui.QGridLayout()
        # self.gridlayout.setHorizontalSpacing(0)

        self.FindID = QtGui.QLineEdit()
        self.LocusID = QtGui.QLineEdit()
        SampleID = QtGui.QLineEdit()

        self.SampleDescription = QtGui.QPlainTextEdit()

        self.savesample = QtGui.QPushButton()
        self.savesample.setText("Save")
        self.savesample.setFixedWidth(150)
        # selayout_homepage.addWidget(saveproject)
        self.map = QtGui.QPushButton('Map')
        self.map.setFixedWidth(150)


        #
        self.gridlayout.addWidget(QtGui.QLabel('Sample ID', self), 1, 0)
        self.gridlayout.addWidget(SampleID, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Locus ID', self), 2, 0)
        self.gridlayout.addWidget(self.LocusID, 2, 1)


        self.gridlayout.addWidget(QtGui.QLabel('Description', self), 3, 0)
        self.gridlayout.addWidget(self.SampleDescription, 3, 1)

        self.gridlayout.setRowStretch(4, 1)


        self.gridlayout.addWidget(self.savesample, 5, 2)
        self.gridlayout.addWidget(self.map, 5, 1)


        # self.gridlayout.addWidget(QtGui.QLabel('', self), 12, 0)
        self.gridlayout.setRowStretch(13, 1)
        self.setLayout(self.gridlayout)
        self.resize(300, 200)
        # self.setWindowTitle('Add New Project')

        '''set tab name '''
        self.setTabText(0, "Sample Locus")
        self.tab1.setLayout(self.gridlayout)


    def tab2UI(self):
        self.tab2UIgridlayout = QtGui.QGridLayout()
        # self.gridlayout.setHorizontalSpacing(0)

        self.FindID = QtGui.QLineEdit()
        self.LocusID = QtGui.QLineEdit()
        SampleID = QtGui.QLineEdit()

        self.SampleDescription = QtGui.QPlainTextEdit()

        self.savesample = QtGui.QPushButton()
        self.savesample.setText("Save")
        self.savesample.setFixedWidth(150)

        self.map = QtGui.QPushButton('Map')
        self.map.setFixedWidth(150)
        # selayout_homepage.addWidget(saveproject)
        #
        self.tab2UIgridlayout.addWidget(QtGui.QLabel('Sample ID', self), 1, 0)
        self.tab2UIgridlayout.addWidget(SampleID, 1, 1)

        self.tab2UIgridlayout.addWidget(QtGui.QLabel('Find ID', self), 2, 0)
        self.tab2UIgridlayout.addWidget(self.FindID, 2, 1)


        self.tab2UIgridlayout.addWidget(QtGui.QLabel('Description', self), 3, 0)
        self.tab2UIgridlayout.addWidget(self.SampleDescription, 3, 1)

        self.tab2UIgridlayout.setRowStretch(4, 1)


        self.tab2UIgridlayout.addWidget(self.savesample, 5, 2)
        self.tab2UIgridlayout.addWidget(self.map, 5, 1)

        # self.gridlayout.addWidget(QtGui.QLabel('', self), 12, 0)
        self.tab2UIgridlayout.setRowStretch(13, 1)
        self.setLayout(self.tab2UIgridlayout)
        self.resize(300, 200)
        # self.setWindowTitle('Add New Project')


        self.setTabText(1, "Sample Find")
        self.tab2.setLayout(self.tab2UIgridlayout)

