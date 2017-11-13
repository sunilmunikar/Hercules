import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection


class FloorElement(QtGui.QWidget):
    def __init__(self):
        super(FloorElement, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

       # self.LocusIdEntry = QtGui.QLineEdit()
        #self.Face = QtGui.QLineEdit()
      #  self.FloorID = QtGui.QLineEdit()  # combination of locusID + face
        self.FloorElementID = QtGui.QLineEdit()  # combination of locusID + room + floormaterial
        self.FloorWork = QtGui.QLineEdit()  #
        self.FloorElement = QtGui.QLineEdit()  #
        self.FloorElementMaterial = QtGui.QLineEdit()  # closed list

        '''Average Dimensions in cm'''

        self.ElementLength = QtGui.QLineEdit()
        self.ElementLength.setPlaceholderText('in cm')

        self.ElementWidth = QtGui.QLineEdit()
        self.ElementWidth.setPlaceholderText('in cm')

        self.ElementThickness = QtGui.QLineEdit()
        self.ElementThickness.setPlaceholderText('in cm')

        self.ElementComment = QtGui.QPlainTextEdit()


        '''Grid layout settings for a form '''

        # self.gridlayout.addWidget(QtGui.QLabel('Locus Id:', self), 0, 0)
        # self.gridlayout.addWidget(self.LocusIdEntry, 0, 1)
        #
        # self.gridlayout.addWidget(QtGui.QLabel('Floor ID:', self), 1, 0)
        # self.gridlayout.addWidget(self.FloorID, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Floor Element ID:', self), 1, 0)
        self.gridlayout.addWidget(self.FloorElementID, 1, 1)
        self.gridlayout.addWidget(QtGui.QLabel('Floor Work:', self), 1, 2)
        self.gridlayout.addWidget(self.FloorWork, 1, 3, 1, 1)


        self.gridlayout.addWidget(QtGui.QLabel('Element:', self), 2, 0)
        self.gridlayout.addWidget(self.FloorElement, 2, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Element material:', self), 3, 0)
        self.gridlayout.addWidget(self.FloorElementMaterial, 3, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Element Length:', self), 7, 0)
        self.gridlayout.addWidget(self.ElementLength, 7, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Element Width :', self), 7, 2)
        self.gridlayout.addWidget(self.ElementWidth, 7, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Element Thicknes:', self), 7, 4)
        self.gridlayout.addWidget(self.ElementThickness, 7, 5)

        self.gridlayout.addWidget(QtGui.QLabel('Element Comment:', self), 18, 0)
        self.gridlayout.addWidget(self.ElementComment, 18, 1)


        self.gridlayout.setRowStretch(21, 1)


        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.gridlayout.addWidget(self.saveButton, 22, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 22, 5, 1, 2)
       # self.gridlayout.addWidget(self.showButton, 15, 1, 1, 2)

        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Horizontal Elevation: Floor Element ')
# #
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = FloorElement()
#     main.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()
