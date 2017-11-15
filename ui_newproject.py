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

        '''making the buttons mutually exclusive and adding the event'''
        self.ProjectType = QtGui.QHBoxLayout()
        self.b1 = QtGui.QRadioButton("Archaeological Project")
        self.b1.setChecked(True)
        #self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
        self.ProjectType.addWidget(self.b1)

        self.b2 = QtGui.QRadioButton("Fieldwork Activity")
       # self.b2.toggled.connect(lambda: self.btnstate(self.b2))
        self.ProjectType.addWidget(self.b2)

        #putting the button in the group makes it mutually exclusive
        self.ButtonGroup = QtGui.QButtonGroup()
        self.ButtonGroup.addButton(self.b1, 1)
        self.ButtonGroup.addButton(self.b2, 2)


       # self.ProjectType.addWidget(QtGui.QRadioButton("Archaeological Project"))
        #self.ProjectType.addWidget(QtGui.QRadioButton("Fieldwork Activity"))

        self.ArchaeologicalProjectType = QtGui.QVBoxLayout()
        self.ArchaeologicalProjectType.addWidget(QtGui.QCheckBox("Sagalassos"))
        self.ArchaeologicalProjectType.addWidget(QtGui.QCheckBox("Other"))



        self.FieldworkActivitySubType = QtGui.QComboBox()
        self.FieldworkActivitySubType.setFixedWidth(200)
        self.FieldworkActivitySubType.addItems(['Extensive Survey', 'Interdisciplinary Research', 'Intensive Survey',
                                                'Excavation', 'Study', 'Building', 'Monument'])



        self.FieldworkActivityType = QtGui.QVBoxLayout()
        self.FieldworkActivityType.addWidget(QtGui.QCheckBox("Study Region"))
        self.FieldworkActivityType.addWidget(QtGui.QCheckBox("Town"))
        self.FieldworkActivityType.addWidget(self.FieldworkActivitySubType)



        self.ProjectLabel = QtGui.QLabel("Project Type:")

        #self.ArchaeologicalProject = QtGui.QCheckBox("Archaeological Project")
        #self.FieldworkActivity = QtGui.QCheckBox("Fieldwork Activity")
        #



        #self.FieldworkActivityType.setFixedWidth(200)


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
        self.gridlayout.addLayout(self.ProjectType, 1, 1, 1, 3)
        self.gridlayout.addLayout(self.ArchaeologicalProjectType, 3, 1, 1, 2)
        self.gridlayout.addLayout(self.FieldworkActivityType, 3, 2, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('**************************************************************', self), 4, 1, 1, 7)
        self.gridlayout.setRowStretch(5, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Site :', self), 6, 0)
        self.gridlayout.addWidget(self.site, 6, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Date:', self), 7, 0)
        self.gridlayout.addWidget(self.date, 7, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Study Area:', self), 8, 0)
        self.gridlayout.addWidget(self.studyArea, 8, 1)
        self.gridlayout.setRowStretch(10, 1)



        self.gridlayout.addWidget(self.saveproject, 11, 2)
        #self.gridlayout.addWidget(QtGui.QLabel('', self), 12, 0)
        self.gridlayout.setRowStretch(13, 1)
        self.setLayout(self.gridlayout)
        self.resize(300, 200)
        #self.setWindowTitle('Add New Project')




















