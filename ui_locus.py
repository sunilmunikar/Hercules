import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

from PyQt4 import QtSql
from sqlite3 import dbapi2 as db

from PyQt4.QtSql import QSqlTableModel


#
# CONFIG_DATABASE_PATH = "./"
# CONFIG_DATABASE_NAME = "SIIS_2017.sqlite"
# filename = os.path.join(CONFIG_DATABASE_PATH,
#                         CONFIG_DATABASE_NAME)
# db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
# db.setDatabaseName(filename)


class Locus(QtGui.QWidget):
    def __init__(self):
        super(Locus, self).__init__()

        #self.gridlayout = QtGui.QGridLayout()
        self.layout = QtGui.QGridLayout()


        self.LocusIdEntry = QtGui.QLineEdit()

        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_locusType")
        self.model.select()
        self.LocusType = QtGui.QComboBox()
        self.LocusType.setModel(self.model)
        self.LocusType.setModelColumn(self.model.fieldIndex("LABEL"))
        LocusTypeLabel = QLabel("&Type:")
        LocusTypeLabel.setBuddy(self.LocusType)

        self.LocusSubType1Select = QtGui.QComboBox()
        self.LocusSubType2Select = QtGui.QComboBox()
        self.LocusSubType3Select = QtGui.QComboBox()

        self.SectorTrenchEntry = QtGui.QLineEdit()
        self.SpaceRoomEntry = QtGui.QLineEdit()
        self.LocusDescription = QtGui.QPlainTextEdit()
        self.LocusDescription.setFixedHeight(100)

        """Set the layout"""

        self.layout.addWidget(QtGui.QLabel('Locus Number:', self), 0, 0)
        self.layout.addWidget(self.LocusIdEntry, 0, 1)

        self.layout.addWidget(QtGui.QLabel('Locus Type:', self), 1, 0)
        self.layout.addWidget(self.LocusType, 1, 1, )

        self.layout.addWidget(QtGui.QLabel('Locus SubType1:', self), 2, 0)
        self.layout.addWidget(self.LocusSubType1Select, 2, 1)
        # self.layout.setColumnMinimumWidth(1, 1)


        self.layout.addWidget(QtGui.QLabel('Locus SubType2:', self), 3, 0)
        self.layout.addWidget(self.LocusSubType2Select, 3, 1)

        self.layout.addWidget(QtGui.QLabel('Locus SubType3:', self), 4, 0)
        self.layout.addWidget(self.LocusSubType3Select, 4, 1)

        self.layout.addWidget(QtGui.QLabel('Sector/ Trench:', self), 7, 0)
        self.layout.addWidget(self.SectorTrenchEntry, 7, 1, 1, 1)

        self.layout.addWidget(QtGui.QLabel('Space/ Room:', self), 8, 0)
        self.layout.addWidget(self.SpaceRoomEntry, 8, 1, 1, 1)

        self.layout.addWidget(QtGui.QLabel('Description:', self), 9, 0)
        self.layout.addWidget(self.LocusDescription, 9, 1, 1, 8)

        self.map = QtGui.QPushButton('Map', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.addButton = QtGui.QPushButton('Add New', self)

        self.layout.addWidget(self.map, 11, 0)
        self.layout.addWidget(self.saveButton, 11, 4)
        self.layout.addWidget(self.cancelButton, 11, 6)
        self.layout.addWidget(self.addButton, 11, 2)


        self.setLayout(self.layout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Horizontal Elevation: Superstructure Element ')
#
def main():
    app = QtGui.QApplication(sys.argv)
    main = Locus()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

