import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection


class VAshlarSurTreatment(QtGui.QWidget):
    def __init__(self):
        super(VAshlarSurTreatment, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.LocusIdEntry = QtGui.QLineEdit()
        self.CourseID = QtGui.QLineEdit() # combination of locusID + face+ construction subtype
        self.SurfaceTreatment = QtGui.QPlainTextEdit()

        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)


        self.gridlayout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.gridlayout.addWidget(self.LocusIdEntry, 0, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Course ID:', self), 1, 0)
        self.gridlayout.addWidget(self.CourseID, 1, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Surface Treatment:', self), 2, 0)
        self.gridlayout.addWidget(self.SurfaceTreatment, 2, 1, 1, 2)



        self.gridlayout.addWidget(self.saveButton, 12, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 12, 5, 1, 2)


        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Vertical Elevation: Ashlar Surface Treatment')

#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = VAshlarSurTreatment()
#
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
