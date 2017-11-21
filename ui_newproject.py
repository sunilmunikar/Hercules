import sys
from PyQt4 import QtGui, QtCore


class NewProject(QtGui.QWidget): #Changed form directly declaring it as a class)
    def __init__(self):
        super(NewProject, self).__init__()

    #def setupUi(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.lightGray)
        self.setPalette(p)

        self.gridlayout = QtGui.QGridLayout()
        #self.gridlayout.setHorizontalSpacing(0)

        self.Face = QtGui.QLineEdit()

        self.ProjectTitle = QtGui.QLineEdit()

        '''Creating the buttons and adding them to Vertical Box Layout'''
        self.ProjectType = QtGui.QHBoxLayout()
        self.b1 = QtGui.QRadioButton("Archaeological Project")
        #self.b1.setChecked(True)
        self.b2 = QtGui.QRadioButton("Fieldwork Activity")

        self.ProjectType.addWidget(self.b1)
        self.ProjectType.addWidget(self.b2)


        '''Putting the button in the group to make it mutually exclusive '''
        self.ButtonGroupProjectType = QtGui.QButtonGroup()
        self.ButtonGroupProjectType.addButton(self.b1, 1)
        self.ButtonGroupProjectType.addButton(self.b2, 2)

        # self.b2.toggled.connect(lambda: self.btnstate(self.b2))

        #self.ProjectType.addWidget(self.ButtonGroup)

       # self.ProjectType.addWidget(QtGui.QRadioButton("Archaeological Project"))
        #self.ProjectType.addWidget(QtGui.QRadioButton("Fieldwork Activity"))

        '''Creating the buttons and adding them to Vertical Box Layout'''
        self.ArchaeologicalProjectType = QtGui.QVBoxLayout()
        self.b1a = QtGui.QCheckBox("Sagalassos")
        self.b1b = QtGui.QCheckBox("Other")

        self.ArchaeologicalProjectType.addWidget(self.b1a)
        self.ArchaeologicalProjectType.addWidget(self.b1b)

        '''Creating the buttons and adding them to Vertical Box Layout'''
        self.FieldworkActivityType = QtGui.QVBoxLayout()
        self.b2a = QtGui.QCheckBox("Study Region")
        self.b2b = QtGui.QCheckBox("Town")
        self.FieldworkActivityType.addWidget(self.b2a)
        self.FieldworkActivityType.addWidget(self.b2b)

        '''Putting the button in the group to make it mutually exclusive '''
        self.ButtonGroupSubType = QtGui.QButtonGroup()
        self.ButtonGroupSubType.addButton(self.b1a, 1)
        self.ButtonGroupSubType.addButton(self.b1b, 2)
        self.ButtonGroupSubType.addButton(self.b2a, 1)
        self.ButtonGroupSubType.addButton(self.b2b, 2)



        '''Putting the button in the group to make it mutually exclusive '''
        self.ButtonGroupFieldType = QtGui.QButtonGroup()



        #self.ArchaeologicalProjectType.addWidget(QtGui.QCheckBox("Sagalassos"))
        #self.ArchaeologicalProjectType.addWidget(QtGui.QCheckBox("Other"))

        self.FieldworkActivitySubType = QtGui.QComboBox()
        self.FieldworkActivitySubType.setFixedWidth(200)
        self.FieldworkActivitySubType.addItems(['Extensive Survey', 'Interdisciplinary Research', 'Intensive Survey',
                                                'Excavation', 'Study', 'Building', 'Monument'])
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

        self.gridlayout.addWidget(QtGui.QLabel('Year:', self), 7, 0)
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


