import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection



class Project(QtGui.QWidget):
    def __init__(self):
        super(Project, self).__init__()

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.lightGray)
        self.setPalette(p)

        self.gridlayout = QtGui.QGridLayout()
        #self.gridlayout.setHorizontalSpacing(0)

        self.ProjectName = QtGui.QLineEdit()
        self.LocusID = QtGui.QLineEdit()


        self.ProjectNameBox = QtGui.QListView()


        self.LocusIDBox = QtGui.QListView()
        self.model = QtGui.QStandardItemModel(self.LocusIDBox)
        ID = ['SA-2017-UAS-0001',
              'SA-2017-UAS-0002',
              'SA-2017-UAS-0003'

              ]
        for index in ID:
            items = QtGui.QStandardItem(index)
            #items.setCheckable(True)
            self.model.appendRow(items)
        self.LocusIDBox.setModel(self.model)

        self.ProjectNameLabel = QtGui.QLabel("Project Name:")
        self.LocusIDLabel = QtGui.QLabel("Locus ID :")

        self.saveproject = QtGui.QPushButton()
        self.saveproject.setText("Save Project")
        self.saveproject.setFixedWidth(150)
        #selayout_homepage.addWidget(saveproject)


        self.gridlayout.addWidget(QtGui.QLabel('Shows the list of  last recent "Projects" and "Locus ID" ', self), 0, 0, 1, 4)


        self.gridlayout.addWidget(self.ProjectNameLabel, 2, 1)
        self.gridlayout.addWidget(self.LocusIDLabel, 2, 3, 1, 4)



        self.gridlayout.addWidget(self.ProjectNameBox, 4, 1)
        self.gridlayout.addWidget(self.LocusIDBox, 4, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Search: ', self), 5, 0, 1, 4)

        self.gridlayout.addWidget(self.ProjectName, 6, 1)
        self.ProjectName.setPlaceholderText('Search the project Name')
        self.LocusID.setPlaceholderText('Search the Locus Id')


        self.gridlayout.addWidget(self.LocusID, 6, 3)


        #self.gridlayout.addWidget(self.saveproject, 11, 2)
        #self.gridlayout.addWidget(QtGui.QLabel('', self), 12, 0)
        self.gridlayout.setRowStretch(13, 1)
        self.setLayout(self.gridlayout)
        self.resize(300, 200)
        #self.setWindowTitle('Add New Project')




















