import os
import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtSql
import sqlite3
from sqlite3 import dbapi2 as db

from PyQt4.QtSql import QSqlTableModel

from spatialiteConnection import SpatialiteDbConnect


class Locus(QtGui.QWidget):
    def __init__(self):
        super(Locus, self).__init__()

        self.layout = QtGui.QGridLayout()
        self.LocusIdEntry = QtGui.QLineEdit()

        #     # Create model
        self.locusTypeModel = QSqlTableModel(self)
        self.locusTypeModel.setTable("tbl_locusType")
        self.locusTypeModel.select()

        self.locusSubType1Model = QSqlTableModel(self)
        self.locusSubType1Model.setTable("tbl_locus_subtype1")
        #self.locusSubType1Model.select()

        self.locusSubType2Model = QSqlTableModel(self)
        self.locusSubType2Model.setTable("tbl_locus_subtype2")

        self.locusSubType3Model = QSqlTableModel(self)
        self.locusSubType3Model.setTable("tbl_locus_subtype3")


        # Create combo and set its model
        self.locusType = self.createCombobox(self.locusTypeModel, "typeLabel")
        self.locusSubType1 = self.createCombobox(self.locusSubType1Model, "subtype1Label")
        self.locusSubType2 = self.createCombobox(self.locusSubType2Model, "subtype2Label")
        self.locusSubType3 = self.createCombobox(self.locusSubType3Model, "subtype3Label")

        self.SectorTrenchEntry = QtGui.QLineEdit()
        self.SpaceRoomEntry = QtGui.QLineEdit()
        self.LocusDescription = QtGui.QPlainTextEdit()
        self.LocusDescription.setFixedHeight(100)




        """Set the layout"""

        self.layout.addWidget(QtGui.QLabel('Locus Number:', self), 0, 0)
        self.layout.addWidget(self.LocusIdEntry, 0, 1)

        self.layout.addWidget(QtGui.QLabel('Locus Type:', self), 1, 0)
        self.layout.addWidget(self.locusType, 1, 1, )

        self.layout.addWidget(QtGui.QLabel('Locus SubType1:', self), 2, 0)
        self.layout.addWidget(self.locusSubType1, 2, 1)
        # self.layout.setColumnMinimumWidth(1, 1)


        self.layout.addWidget(QtGui.QLabel('Locus SubType2:', self), 3, 0)
        self.layout.addWidget(self.locusSubType2, 3, 1)

        self.layout.addWidget(QtGui.QLabel('Locus SubType3:', self), 4, 0)
        self.layout.addWidget(self.locusSubType3, 4, 1)

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
        self.setWindowTitle('Locus')


        self.locusType.setCurrentIndex(-1)

        self.locusType.currentIndexChanged.connect( self.subType1selection)
        self.locusSubType1.currentIndexChanged.connect(self.subType2selection)
        self.locusSubType2.currentIndexChanged.connect(self.subType3selection)


    @staticmethod
    def createCombobox(model, modelColumn):
        locusTypeComboBox = QtGui.QComboBox()
        locusTypeComboBox.setModel(model)
        locusTypeComboBox.setModelColumn(model.fieldIndex(modelColumn))
        return locusTypeComboBox


    pyqtSlot('int')

    #def locusSubType1clear(self):

    def subType1selection(self, index):
        locusTypeModelIndex = self.locusTypeModel.index(index, self.locusTypeModel.fieldIndex("typeID"))
        data = self.locusTypeModel.data(locusTypeModelIndex)

        filter = QString("typeID=%1").arg(data.toPyObject())
        self.locusSubType1Model.setFilter(filter)
        self.locusSubType1Model.select()
        print data.toPyObject()

    def subType2selection(self, index):

        locusSubType1ModelIndex = self.locusSubType1Model.index(index, self.locusSubType1Model.fieldIndex("subtype1ID"))
        data = self.locusSubType1Model.data(locusSubType1ModelIndex)

        filter = QString("subtype1ID= %1").arg(data.toPyObject())
        self.locusSubType2Model.setFilter(filter)
        self.locusSubType2Model.select()
        # print data.toPyObject()
        # print data

    def subType3selection(self, index):
        locusSubType2ModelIndex = self.locusSubType2Model.index(index, self.locusSubType2Model.fieldIndex("subtype2ID"))
        data = self.locusSubType2Model.data(locusSubType2ModelIndex)

        filter = QString("subtype2ID=%1").arg(data.toPyObject())
        self.locusSubType3Model.setFilter(filter)
        self.locusSubType3Model.select()
        print data.toPyObject()



def main():
    app = QtGui.QApplication(sys.argv)

    connection = SpatialiteDbConnect()
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(connection.filename)
    if not db.open():
        QtGui.QMessageBox.warning(None, "Combo Box Example",
                                  QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    # Would normally be invoked as modal dialog.
    # But for simplicity we use it as the main form here.
    main = Locus()
    main.show()
    app.exec_()
    # del form
    del db


if __name__ == '__main__':
    main()
