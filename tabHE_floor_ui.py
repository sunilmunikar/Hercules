import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection
from tabHE_floorelement_ui import *


class Floor(QtGui.QWidget):
    def __init__(self):
        super(Floor, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.LocusIdEntry = QtGui.QLineEdit()
        #self.Face = QtGui.QLineEdit()
        self.FloorID = QtGui.QLineEdit()  # combination of locusID + face
        self.RoomSpace = QtGui.QLineEdit()  # combination of locusID + face


        '''combo box later to be replaced from the datatype from the spatialite database'''
       # self.ConstructionTechnique = QtGui.QComboBox()  # closed list
        self.FloorMaterial = QtGui.QComboBox()  # closed list
        self.FloorWork = QtGui.QComboBox()  # closed list
        self.Function = QtGui.QComboBox()  # closed list
        self.WalkingLevel = QtGui.QComboBox()  # closed list



        self.StoneType = QtGui.QHBoxLayout()
        self.StoneType.addWidget(QtGui.QCheckBox("Limestone"))
        self.StoneType.addWidget(QtGui.QCheckBox("Marble"))
        self.StoneType.addWidget(QtGui.QCheckBox("Purple schist"))

        self.Bedding = QtGui.QHBoxLayout()
        self.Bedding.addWidget(QtGui.QRadioButton("Earth"))
        self.Bedding.addWidget(QtGui.QRadioButton("Mortared"))

        self.Joints = QtGui.QHBoxLayout()
        self.Joints.addWidget(QtGui.QRadioButton("Dry"))
        self.Joints.addWidget(QtGui.QRadioButton("Mortared"))


        '''Average Dimensions in cm'''

        self.Length = QtGui.QLineEdit()
        self.Length.setPlaceholderText('in cm')

        self.Width = QtGui.QLineEdit()
        self.Width.setPlaceholderText('in cm')

        self.Thickness = QtGui.QLineEdit()
        self.Thickness.setPlaceholderText('in cm')

        self.Color = QtGui.QLineEdit()
        self.Texture = QtGui.QLineEdit()
        self.GeneralComment = QtGui.QPlainTextEdit()


        '''Grid layout settings for a form '''

        self.gridlayout.addWidget(QtGui.QLabel('Locus Id:', self), 0, 0)
        self.gridlayout.addWidget(self.LocusIdEntry, 0, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Floor ID:', self), 1, 0)
        self.gridlayout.addWidget(self.FloorID, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Room/ Space:', self), 2, 0)
        self.gridlayout.addWidget(self.RoomSpace, 2, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Length:', self), 7, 0)
        self.gridlayout.addWidget(self.Length, 7, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Width :', self), 7, 2)
        self.gridlayout.addWidget(self.Width, 7, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Thicknes:', self), 7, 4)
        self.gridlayout.addWidget(self.Thickness, 7, 5)

        self.gridlayout.addWidget(QtGui.QLabel('Floor Material:', self), 8, 0)
        self.gridlayout.addWidget(self.FloorMaterial, 8, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Floor Work:', self), 10, 0)
        self.gridlayout.addWidget(self.FloorWork, 10, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Stone Type:', self), 11, 0)
        self.gridlayout.addLayout(self.StoneType, 11, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Bedding:', self), 12, 0)
        self.gridlayout.addLayout(self.Bedding, 12, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Joints:', self), 12, 2)
        self.gridlayout.addLayout(self.Joints, 12, 3, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Color:', self), 15, 0) #in mm
        self.gridlayout.addWidget(self.Color, 15, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Texture:', self), 15, 2)  # cm
        self.gridlayout.addWidget(self.Texture, 15, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Function:', self), 16, 0)  # cm
        self.gridlayout.addWidget(self.Function, 16, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Walking Level:', self), 17, 0)  # cm
        self.gridlayout.addWidget(self.WalkingLevel, 17, 1)

        self.gridlayout.addWidget(QtGui.QLabel('General Comment:', self), 18, 0)
        self.gridlayout.addWidget(self.GeneralComment, 18, 1)


        self.gridlayout.setRowStretch(21, 1)

        self.AddElement = QtGui.QPushButton('Add Floor Element', self)

        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.gridlayout.addWidget(self.saveButton, 22, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 22, 5, 1, 2)
        self.gridlayout.addWidget(self.AddElement, 22, 1, 1, 2)

        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Horizontal Elevation: Floor ')

        self.connect(self.AddElement, QtCore.SIGNAL('clicked()'), self.addFloorElement)

    def addFloorElement(self):
        self.FloorElement = FloorElement()
        self.FloorElement.show()


# #
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = Floor()
#     main.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()
