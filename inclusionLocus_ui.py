import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection



class InclusionLocus(QtGui.QWidget):
    def __init__(self):
        super(InclusionLocus, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.InclusionID = QtGui.QLineEdit()
        self.locusID = QtGui.QLineEdit()
        self.NatureInclusions = QtGui.QLineEdit()


        self.sizeInclusions = QtGui.QHBoxLayout()
        self.sizeInclusions.addWidget(QtGui.QCheckBox("Small"))
        self.sizeInclusions.addWidget(QtGui.QCheckBox("Very small"))
        self.sizeInclusions.addWidget(QtGui.QCheckBox("Medium"))
        self.sizeInclusions.addWidget(QtGui.QCheckBox("Large"))
        self.sizeInclusions.addWidget(QtGui.QCheckBox("Very large"))

        self.quantityInclusions = QtGui.QHBoxLayout()
        self.quantityInclusions.addWidget(QtGui.QCheckBox("Rare"))
        self.quantityInclusions.addWidget(QtGui.QCheckBox("Sparse"))
        self.quantityInclusions.addWidget(QtGui.QCheckBox("Medium"))
        self.quantityInclusions.addWidget(QtGui.QCheckBox("Common"))
        self.quantityInclusions.addWidget(QtGui.QCheckBox("Very Common"))


        self.gridlayout.addWidget(QtGui.QLabel('Loous ID:', self), 0, 0)
        self.gridlayout.addWidget(self.locusID, 0, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Inclusions ID:', self), 1, 0)
        self.gridlayout.addWidget(self.InclusionID, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Nature Inclusions:', self), 2, 0)
        self.gridlayout.addWidget(self.NatureInclusions, 2, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Size Inclusions:', self), 3, 0)
        self.gridlayout.addLayout(self.sizeInclusions, 3, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Quantity Inclusions:', self), 4, 0)
        self.gridlayout.addLayout(self.quantityInclusions, 4, 1)


        self.gridlayout.setRowStretch(7, 1)

       # self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.gridlayout.addWidget(self.saveButton, 15, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 15, 5, 1, 2)
        #self.gridlayout.addWidget(self.showButton, 15, 1, 1, 2)

        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('More on Locus Inclusion Details')




# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = ArchitecturalFeature()
#
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
