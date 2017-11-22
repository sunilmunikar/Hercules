import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
import sqlite3
from sqlite3 import dbapi2 as db

from PyQt4.QtSql import QSqlTableModel

from spatialiteConnection import SpatialiteDbConnect

CONFIG_DATABASE_PATH = "./"
CONFIG_DATABASE_NAME = "SIIS_2017.sqlite"


class EditItemDlg(QDialog):
    def __init__(self, parent=None):
        super(EditItemDlg, self).__init__(parent)
        #     # Create model
        self.locusTypeModel = QSqlTableModel(self)
        self.locusTypeModel.setTable("tbl_locusType")
        self.locusTypeModel.select()

        # Create combo and set its model
        self.locusTypeComboBox = self.createCombobox(self.locusTypeModel, "typeLabel")
        typeLabel = QLabel("&Type:")
        typeLabel.setBuddy(self.locusTypeComboBox)

        #     # Create model
        self.locusSubTypeModel = QSqlTableModel(self)
        self.locusSubTypeModel.setTable("tbl_locus_subType1")
        self.locusSubTypeModel.select()

        # Create combo and set its model
        self.locusSubTypeCombobox = self.createCombobox(self.locusSubTypeModel, "subtype1Label")
        #
        # self.locusSubTypeCombobox = QComboBox()
        # self.locusSubTypeCombobox.setModel(self.locusSubTypeModel)
        # self.locusSubTypeCombobox.setModelColumn(
        #     self.locusTypeModel.fieldIndex("label"))

        #     # Create model
        # self.locusSubType2Model = QSqlTableModel(self)
        # self.locusSubType2Model.setTable("tbl_locus_subType1")
        # self.locusSubType2Model.select()

        controlLayout = QGridLayout()
        controlLayout.addWidget(self.locusTypeComboBox, 4, 0)
        controlLayout.addWidget(self.locusSubTypeCombobox, 5, 0)

        self.setLayout(controlLayout)
        self.resize(500, 125)

        self.locusTypeComboBox.currentIndexChanged.connect(self.f)

    @staticmethod
    def createCombobox(model, modelColumn):
        locusTypeComboBox = QComboBox()
        locusTypeComboBox.setModel(model)
        locusTypeComboBox.setModelColumn(model.fieldIndex(modelColumn))
        return locusTypeComboBox

    pyqtSlot('int')

    def f(self, index):
        locusTypeModelIndex = self.locusTypeModel.index(index, self.locusTypeModel.fieldIndex("typeID"))
        # idx = self.locusTypeComboBox.model().index(index, self.locusTypeModel.fieldIndex("ID"))
        data = self.locusTypeModel.data(locusTypeModelIndex)

        filter = QString("subtype1ID=%1").arg(data.toPyObject())
        self.locusSubTypeModel.setFilter(filter)
        self.locusSubTypeModel.select()
        print data.toPyObject()


def main():
    app = QApplication(sys.argv)

    filename = os.path.join(CONFIG_DATABASE_PATH,
                            CONFIG_DATABASE_NAME)
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Combo Box Example",
                            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    # Would normally be invoked as modal dialog.
    # But for simplicity we use it as the main form here.
    form = EditItemDlg()
    form.show()
    app.exec_()
    del form
    del db


if __name__ == '__main__':
    main()
