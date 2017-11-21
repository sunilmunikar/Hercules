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
    #    # self.setWindowTitle("Edit Phone Number")
    #
    #     # Create model
        self.model = QSqlTableModel(self)
        self.model.setTable("tbl_locusType")
        self.model.select()

        # Create combo and set its model
        self.typeComboBox = QComboBox()
        self.typeComboBox.setModel(self.model)
        self.typeComboBox.setModelColumn(
                          self.model.fieldIndex("LABEL"))
        typeLabel = QLabel("&Type:")
        typeLabel.setBuddy(self.typeComboBox)

        self.model2 = QSqlTableModel(self)
        self.model2.setTable("tbl_locus_subType1")
        self.model2.select()
        self.model2.setFilter("")

        self.combobox_3 = QComboBox()
        # Create combo and set its model
        #self.typeComboBox = QComboBox()
        self.combobox_3.setModel(self.model2)
        self.combobox_3.setModelColumn(
            self.model.fieldIndex("LABEL"))





        #labeltype = self.model2.setMfieldIndex("locusType")
        #typeLabel = QLabel("&Type:")
        #typeLabel.setBuddy(self.typeComboBox)

        # listc={}
        #
        # for LABEL, locusType in self.model2:
        #     listc.setdefault(locusType, []).append(LABEL)
        #    # lista.setdefault(locusType)
        # print listc
        # self.items = listc
        # print self.items







        self.combobox_1 = QComboBox()
        #self.combobox_1 = self.typeComboBox.setModelColumn(
            #self.model.fieldIndex("LABEL"))



        self.combobox_2 = QComboBox()
       # self.combobox_3 = QComboBox()


        controlLayout = QGridLayout()
        controlLayout.addWidget(self.typeComboBox, 4, 0 )

       # controlLayout.addWidget(self.combobox_1, 2, 0 )
        #controlLayout.addWidget(self.combobox_2, 3, 0 )
        controlLayout.addWidget(self.combobox_3, 5, 0 )

        self.setLayout(controlLayout)
        self.resize(500, 125)






        # self.combobox_1.addItems(['8', '9', '20'])        #
        # self.items = {'1': ['a', 'b', 'c'], '2': ['d', 'e', 'f'], '3': ['g', 'h', 'i']}
        # self.items_2 = {'c': ['aa', 'bb', 'cc']}

        '''connnecting to the db 
                    for dictnary key values for combobox 2'''

        self.connection = db.connect('SIIS_2017.sqlite')
        cursor = self.connection.cursor()

        cursor.execute('SELECT LABEL FROM tbl_locusType')
        locusType = cursor.fetchall()
        print locusType
        '''Convert to Qsrtring list '''

        qstringList = QStringList()
        for LABEL in locusType:
            qstringList.append(QString(LABEL[0]))

        self.combobox_1.addItems(qstringList)



        cursor.execute('SELECT LABEL,locusType FROM tbl_locus_subtype1')
        result = cursor.fetchall()

        listb = {}
        for LABEL, locusType in result:
            listb.setdefault(locusType, []).append(LABEL)
           # lista.setdefault(locusType)
        print listb
        self.items = listb
        print self.items

        # self.combobox_1 = self.itemslocusType
        #self.combobox_1.addItems(str[self.itemslocusType])


        # self.combobox_1.activated[str].connect(self.on_combo_activated)

        self.combobox_1.activated[str].connect(self.on_combo_activated)
        self.typeComboBox.currentIndexChanged.connect(self.f)



        #self.combobox_1.activated[str].connect(self.on_combo_activated)
        self.combobox_2.activated[str].connect(self.on_combo2_activated)






    pyqtSlot('int')
    def f(self, index):
        # print "test"
        idx = self.typeComboBox.model().index(index, 1)
        data = self.typeComboBox.model().data(idx)

        self.combobox_3.clear()
        # self.combobox_3.addItems(self.combobox_3.setModelColumn(data))




        # data = self.typeComboBox.itemData(index)
        print data.toPyObject()

            # print 'integer:', data

    # def ButtonClickedText(self):
    #      test = str(self.typeComboBox.value(2, Qt.UserRole))
    #      print test

    def on_combo_activated(self, text):
        self.combobox_2.clear()
        self.combobox_2.addItems(self.items[str(text)])

    def on_combo2_activated(self):
        self.combobox_3.clear()
        self.combobox_3.addItems(self.items_2[str(self.combobox_2.currentText())])


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





    # self.connect(buttonBox, SIGNAL("accepted()"),
    #              self, SLOT("accept()"))
    # self.connect(buttonBox, SIGNAL("rejected()"),
    #              self, SLOT("reject()"))

    # buttonBox.clicked.connect(self.ButtonClickedText)

    # self.typeComboBox.currentIndexChanged.connect(self.f)
