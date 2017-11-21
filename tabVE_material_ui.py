import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection


class VerticalElevationMaterial(QtGui.QWidget):
    def __init__(self):
        super(VerticalElevationMaterial, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.LocusIdEntry = QtGui.QLineEdit()
        self.ID = QtGui.QLineEdit() # combination of locusID + face
        self.Face = QtGui.QComboBox()  # closed list

        self.MaterialType = QtGui.QComboBox()  # closed list
        self.MaterialColor = QtGui.QLineEdit()
        self.MaterialTexture = QtGui.QLineEdit()
        self.IdentificationComment = QtGui.QPlainTextEdit()
        self.IdentificationComment.setFixedHeight(100)

        #self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)


        self.gridlayout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.gridlayout.addWidget(self.LocusIdEntry, 0, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Face ID:', self), 0, 3)
        self.gridlayout.addWidget(self.ID, 0, 4, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Face:', self), 1, 0)
        self.gridlayout.addWidget(self.Face, 1, 1, 1, 2)

        # self.tab5layout.addWidget(QtGui.QLabel('###Enter the data about Material###', self), 3, 0, 1, 5)
        self.gridlayout.addWidget(QtGui.QLabel('Material Type:', self), 5, 0)
        self.gridlayout.addWidget(self.MaterialType, 5, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Material Color:', self), 6, 0)
        self.gridlayout.addWidget(self.MaterialColor, 6, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Material Texture:', self), 6, 3)
        self.gridlayout.addWidget(self.MaterialTexture, 6, 4, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Identification Comment:', self), 8, 0)
        self.gridlayout.addWidget(self.IdentificationComment, 8, 1, 1, 1)

        self.gridlayout.addWidget(self.saveButton, 12, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 12, 5, 1, 2)
        #self.gridlayout.addWidget(self.showButton, 12, 1, 1, 2)


        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Vertical Elevation: Material')

#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = VerticalElevation()
#
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
