import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection
#from tabHE_floorelement_ui import *

from tabHE_superstrelement_ui import *


class Suprestructure(QtGui.QWidget):
    def __init__(self):
        super(Suprestructure, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.LocusIdEntry = QtGui.QLineEdit()
        #self.Face = QtGui.QLineEdit()
        self.SuperStructureID = QtGui.QLineEdit()  # combination of locusID + face
        self.RoomSpace = QtGui.QLineEdit()  # combination of locusID + face


        self.SuperStructureFunction = QtGui.QHBoxLayout()
        self.SuperStructureFunction.addWidget(QtGui.QRadioButton("Roof"))
        self.SuperStructureFunction.addWidget(QtGui.QRadioButton("Upper Floor"))


        self.TileType = QtGui.QHBoxLayout()
        self.TileType.addWidget(QtGui.QCheckBox("tegulae"))
        self.TileType.addWidget(QtGui.QCheckBox("Imbrices"))
        self.TileType.addWidget(QtGui.QCheckBox("Stone tile / stone"))

        self.FillMaterial = QtGui.QHBoxLayout()
        self.FillMaterial.addWidget(QtGui.QCheckBox("Rubble"))
        self.FillMaterial.addWidget(QtGui.QCheckBox("Mortared rubble"))
        self.FillMaterial.addWidget(QtGui.QCheckBox("Mortar"))
        self.FillMaterial.addWidget(QtGui.QCheckBox("Other"))

        '''combo box later to be replaced from the datatype from the spatialite database'''
       # self.ConstructionTechnique = QtGui.QComboBox()  # closed list
        self.ConstructionType = QtGui.QComboBox()  # closed list
        self.ConstructionMaterial = QtGui.QComboBox()  # closed list
        self.InnerFaceMaterial = QtGui.QComboBox()  # closed list
        self.RoofOuterFaceMaterial = QtGui.QComboBox()  # closed list
        self.UpperFloorOuterFaceMaterial = QtGui.QComboBox()  # closed list
        self.TileSubtype = QtGui.QComboBox()  # depends on the selection of the tile type closed list

        '''Average Dimensions in cm'''

        self.Length = QtGui.QLineEdit()
        self.Length.setPlaceholderText('in cm')

        self.Width = QtGui.QLineEdit()
        self.Width.setPlaceholderText('in cm')

        self.Thickness = QtGui.QLineEdit()
        self.Thickness.setPlaceholderText('in cm')

        self.InnerFaceThickness = QtGui.QLineEdit()
        self.InnerFaceThickness.setPlaceholderText('in cm')

        self.OuterFaceThickness = QtGui.QLineEdit()
        self.OuterFaceThickness.setPlaceholderText('in cm')

        self.FillThickness = QtGui.QLineEdit()
        self.FillThickness.setPlaceholderText('in cm')

        self.SuperStructureComment = QtGui.QPlainTextEdit()


        '''Grid layout settings for a form '''

        self.gridlayout.addWidget(QtGui.QLabel('Locus Id:', self), 0, 0)
        self.gridlayout.addWidget(self.LocusIdEntry, 0, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Superstructure ID:', self), 1, 0)
        self.gridlayout.addWidget(self.SuperStructureID, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Room/ Space:', self), 2, 0)
        self.gridlayout.addWidget(self.RoomSpace, 2, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Function:', self), 3, 0)
        self.gridlayout.addLayout(self.SuperStructureFunction, 3, 1, 1, 1)


        self.gridlayout.addWidget(QtGui.QLabel('Length:', self), 7, 0)
        self.gridlayout.addWidget(self.Length, 7, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Width :', self), 7, 2)
        self.gridlayout.addWidget(self.Width, 7, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Thicknes:', self), 7, 4)
        self.gridlayout.addWidget(self.Thickness, 7, 5)

        self.gridlayout.addWidget(QtGui.QLabel('Construction Type:', self), 8, 0)
        self.gridlayout.addWidget(self.ConstructionType, 8, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Construction Material:', self), 8, 2)
        self.gridlayout.addWidget(self.ConstructionMaterial, 8, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Inner Face Material:', self), 11, 0)
        self.gridlayout.addWidget(self.InnerFaceMaterial, 11, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Roof Outer Face Material:', self), 11, 2)
        self.gridlayout.addWidget(self.RoofOuterFaceMaterial, 11, 3)

        self.gridlayout.addWidget(QtGui.QLabel('UpperFloor Outer Face Material:', self), 13, 0)
        self.gridlayout.addWidget(self.UpperFloorOuterFaceMaterial, 13, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Tile Type:', self), 15, 0) #in mm
        self.gridlayout.addLayout(self.TileType, 15, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Tile Subtype:', self), 16, 0)  # cm
        self.gridlayout.addWidget(self.TileSubtype, 16, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Fill Material:', self), 17, 0)  # cm
        self.gridlayout.addLayout(self.FillMaterial, 17, 1)

        self.gridlayout.addWidget(QtGui.QLabel('InnerFace Thickness:', self), 18, 0)  # cm
        self.gridlayout.addWidget(self.InnerFaceThickness, 18, 1)

        self.gridlayout.addWidget(QtGui.QLabel('OuterFace Thickness:', self), 18, 2)  # cm
        self.gridlayout.addWidget(self.OuterFaceThickness, 18, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Fill Thickness:', self), 18, 4)  # cm
        self.gridlayout.addWidget(self.FillThickness, 18, 5)


        self.gridlayout.addWidget(QtGui.QLabel('Comment:', self), 19, 0)
        self.gridlayout.addWidget(self.SuperStructureComment, 19, 1)


        self.gridlayout.setRowStretch(21, 1)

        self.AddElement = QtGui.QPushButton('Add Superstructure Element', self)

        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.gridlayout.addWidget(self.saveButton, 22, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 22, 5, 1, 2)
        self.gridlayout.addWidget(self.AddElement, 22, 1, 1, 2)

        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Horizontal Elevation: Superstructure ')

        self.connect(self.AddElement, QtCore.SIGNAL('clicked()'), self.addSuperElement)

    def addSuperElement(self):
        self.SuperElement = SuperstructureElement()
        self.SuperElement.show()


# #
def main():
    app = QtGui.QApplication(sys.argv)
    main = Suprestructure()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
