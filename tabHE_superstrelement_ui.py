import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection


class SuperstructureElement(QtGui.QWidget):
    def __init__(self):
        super(SuperstructureElement, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

       # self.LocusIdEntry = QtGui.QLineEdit()
        #self.Face = QtGui.QLineEdit()
      #  self.FloorID = QtGui.QLineEdit()  # combination of locusID + face
        self.SuperElementID = QtGui.QLineEdit()  # combination of locusID + room + function + elementmaterial
        #self.FloorWork = QtGui.QLineEdit()  #
        #self.FloorElement = QtGui.QLineEdit()  #
        self.SuperElementMaterial = QtGui.QComboBox()  # closed list
        self.SuperAdditionalElement = QtGui.QComboBox()  # closed list


        '''Average Dimensions in cm'''

        self.ElementLength = QtGui.QLineEdit()
        self.ElementLength.setPlaceholderText('in cm')

        self.ElementWidth = QtGui.QLineEdit()
        self.ElementWidth.setPlaceholderText('in cm')

        self.ElementThickness = QtGui.QLineEdit()
        self.ElementThickness.setPlaceholderText('in cm')

        self.DescriptionAdditionalElement = QtGui.QPlainTextEdit()
        self.ElementComment = QtGui.QPlainTextEdit()


        '''Grid layout settings for a form '''

        # self.gridlayout.addWidget(QtGui.QLabel('Locus Id:', self), 0, 0)
        # self.gridlayout.addWidget(self.LocusIdEntry, 0, 1)
        #
        # self.gridlayout.addWidget(QtGui.QLabel('Floor ID:', self), 1, 0)
        # self.gridlayout.addWidget(self.FloorID, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Super Element ID:', self), 1, 0)
        self.gridlayout.addWidget(self.SuperElementID, 1, 1)
        self.gridlayout.addWidget(QtGui.QLabel('Element Material:', self), 2, 0)
        self.gridlayout.addWidget(self.SuperElementMaterial, 2, 1, 1, 1)


        self.gridlayout.addWidget(QtGui.QLabel('Additional Elements:', self), 2, 2)
        self.gridlayout.addWidget(self.SuperAdditionalElement, 2, 3, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Element Length:', self), 7, 0)
        self.gridlayout.addWidget(self.ElementLength, 7, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Element Width :', self), 7, 2)
        self.gridlayout.addWidget(self.ElementWidth, 7, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Element Thicknes:', self), 7, 4)
        self.gridlayout.addWidget(self.ElementThickness, 7, 5)


        self.gridlayout.addWidget(QtGui.QLabel('Additional Element Description:', self), 8, 0)
        self.gridlayout.addWidget(self.DescriptionAdditionalElement, 8, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Element Comments:', self), 9, 0)
        self.gridlayout.addWidget(self.ElementComment, 9, 1, 1, 2)


        self.gridlayout.setRowStretch(15, 1)


        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.gridlayout.addWidget(self.saveButton, 22, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 22, 5, 1, 2)
       # self.gridlayout.addWidget(self.showButton, 15, 1, 1, 2)

        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Horizontal Elevation: Superstructure Element ')
# #
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = SuperstructureElement()
#     main.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()
