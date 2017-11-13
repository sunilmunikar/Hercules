import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection



class NewProject(QtGui.QWidget):
    def __init__(self):
        super(NewProject, self).__init__()


        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.red)
        self.setPalette(p)

        self.gridlayout = QtGui.QGridLayout()
        #self.gridlayout.setHorizontalSpacing(0)

        self.LocusIdEntry = QtGui.QLineEdit()
        self.Face = QtGui.QLineEdit()


        self.ProjectTitle = QtGui.QLineEdit()
        self.ProjectLabel = QtGui.QLabel("Project Type:")

        self.ArchaeologicalProject = QtGui.QCheckBox("Archaeological Project")
        self.FieldworkActivity = QtGui.QCheckBox("Fieldwork Activity")

        self.ArchaeologicalProjectType = QtGui.QComboBox()
        self.ArchaeologicalProjectType.setFixedWidth(200)


        self.FieldworkActivityType = QtGui.QComboBox()
        self.FieldworkActivityType.setFixedWidth(200)


        self.site = QtGui.QLineEdit()
        self.site.setFixedWidth(200)
        self.date = QtGui.QLineEdit()
        self.date.setFixedWidth(200)


        self.studyArea = QtGui.QLineEdit()
        self.studyArea.setFixedWidth(200)

        self.saveproject = QtGui.QPushButton()
        self.saveproject.setText("Save Project")
        self.saveproject.setFixedWidth(150)
        #selayout_homepage.addWidget(saveproject)


        self.gridlayout.addWidget(QtGui.QLabel('Project Title:', self), 0, 0)
        self.gridlayout.addWidget(self.ProjectTitle, 0, 1, 1, 4)

        self.gridlayout.addWidget(self.ProjectLabel, 1, 0)
        #self.gridlayout.setRowStretch(1, 1)
        #self.gridlayout.setRowStretch(2, 1)




        self.gridlayout.addWidget(self.ArchaeologicalProject, 2, 1)

        #self.gridlayout.setColumnStretch(1, 3)

        self.gridlayout.addWidget(self.FieldworkActivity, 2, 3)
        self.gridlayout.addWidget(self.ArchaeologicalProjectType, 3, 1, 1, 4)
        #
        #
        self.gridlayout.addWidget(self.FieldworkActivityType, 3, 3, 1, 4)
        #self.gridlayout.addWidget(QtGui.QLabel('', self), 4, 0)


        self.gridlayout.addWidget(QtGui.QLabel('Site :', self), 5, 0)
        self.gridlayout.addWidget(self.site, 5, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Date:', self), 6, 0)
        self.gridlayout.addWidget(self.date, 6, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Study Area:', self), 7, 0)
        self.gridlayout.addWidget(self.studyArea, 7, 1)
        self.gridlayout.setRowStretch(8, 1)



        self.gridlayout.addWidget(self.saveproject, 11, 2)
        #self.gridlayout.addWidget(QtGui.QLabel('', self), 12, 0)
        self.gridlayout.setRowStretch(13, 1)
        self.setLayout(self.gridlayout)
        self.resize(300, 200)
        #self.setWindowTitle('Add New Project')




















