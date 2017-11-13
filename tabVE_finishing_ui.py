import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection


class VFinishing(QtGui.QWidget):
    def __init__(self):
        super(VFinishing, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.LocusIdEntry = QtGui.QLineEdit()
        self.FinishingID = QtGui.QLineEdit() # combination of locusID + face+ finishing

        self.FinishingType = QtGui.QComboBox()

        self.FinishigDescription = QtGui.QPlainTextEdit()

        """Finishing Dimension """
        self.FinishingLength = QtGui.QLineEdit()
        self.FinishingLength.setPlaceholderText("in cm")
        self.FinishingHeight = QtGui.QLineEdit()
        self.FinishingHeight.setPlaceholderText('in cm')

        self.FinishigComment = QtGui.QPlainTextEdit()



        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)


        self.gridlayout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.gridlayout.addWidget(self.LocusIdEntry, 0, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Finishing ID:', self), 1, 0)
        self.gridlayout.addWidget(self.FinishingID, 1, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Finishing :', self), 2, 0)
        self.gridlayout.addWidget(self.FinishingType, 2, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Description:', self), 3, 0)
        self.gridlayout.addWidget(self.FinishigDescription, 3, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Length :', self), 4, 0)
        self.gridlayout.addWidget(self.FinishingLength, 4, 1)
        self.gridlayout.addWidget(QtGui.QLabel('Height :', self), 4, 2)
        self.gridlayout.addWidget(self.FinishingHeight, 4, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Comments :', self), 5, 0)
        self.gridlayout.addWidget(self.FinishigComment, 5, 1, 1, 2)




        self.gridlayout.addWidget(self.saveButton, 12, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 12, 5, 1, 2)


        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Vertical Elevation: Finishing ')

#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = VFinishing()
#
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
