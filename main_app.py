import sys
from PyQt4 import QtGui

#from PyQt4.QtGui import *
from PyQt4.QtCore import *

#from PyQt4.QtGui import QListView, QWidget, QApplication, QStandardItemModel, QStandardItem, QLabel

import ui_mainwindow_stacked
import locus_data

#import newproject_ui
from LocusRepository import LocusRepository, Locus
#from postgresConnection import DatabaseConnection
import psycopg2 as mdb
import Locus_entry_ui


#db = DatabaseConnection()
#cur = db.connection.cursor()

# class Second(QtGui.QWidget, newproject_ui.Ui_Form):
#     def __init__(self, parent=None):
#         super(Second, self).__init__(parent)

class AppMainwindow(QtGui.QMainWindow, ui_mainwindow_stacked.Ui_MainWindow):
    # standard code in all the app to call the widget

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        # type: () -> object
        #super(AppMainwindow, self).__init__(parent)
        #QMainWindow.__init__(self)
        self.setupUi(self)

        self.Project.clicked.connect(self.display1)
        self.NewProject.clicked.connect(self.display2)
        self.Locus.clicked.connect(self.display3)
        self.Find.clicked.connect(self.display4)
        self.Sample.clicked.connect(self.display5)



       # self.Map.clicked.connect(self.display4)




        #self.locusentry()








    def display1(self):
            self.stackedWidget.setCurrentIndex(0)

    def display2(self):
        self.stackedWidget.setCurrentIndex(1)

    def display3(self):
        self.stackedWidget.setCurrentIndex(2)

    def display4(self):
        self.stackedWidget.setCurrentIndex(3)

    def display5(self):
        self.stackedWidget.setCurrentIndex(4)

        # self.list_view()
        # self.LocusIdEntry.setPlaceholderText("Enter locus ID ")
        # # find = self.find_id.textChanged.connect()
        # self.Save.clicked.connect(self.save_locus)
        # self.Close.clicked.connect(self.close)
        # self.Update.clicked.connect(self.add_new)

        #self.Update.clicked.connect(self.update_locus)
        #self.ShowAll.clicked.connect(self.ShowAll_clicked)
        #self.dialog = Second(self)

#     def add_new(self):
#         self.LocusIdEntry.setText('')
#         # self.LocusTypeEntry.setItemText(2, locus.locus_type)
#         self.SpaceRoomEntry.setText('')
#         self.SectorTrenchEntry.setText('')
#         self.DescriptionEntry.setPlainText('')
#
#         print 'locus id is :', self.LocusIdEntry.text()
#
#
#
#
#
#
#
#     def list_view(self):
#         list = QListView()
#         # Create an empty model for the list's data
#         # model = QStandardItemModel(list)
#         repo = LocusRepository()
#         locusList = repo.get_all_locus()
#
#         # Create an empty model for the list's data
#         model = QStandardItemModel(list)
#
#         for locus in locusList:
#             # Create an item with a caption
#             item = QStandardItem(locus.locus_id)
#
#             # Add the item to the model
#             model.appendRow(item)
#
#         model.itemChanged.connect(self.on_item_changed)
#
#         #    current_index = 0
#         #    list.currentChanged(current_index)
#         # list.selectionModel().currentChanged.connect(on_current_changed)
#
#         # self.listWidget.itemClicked.connect(self.printItemText)
#         # app.connect(list, SIGNAL("currentChanged()"),
#         #              printItemText)
#
#         # Apply the model to the list view
#         list.setModel(model)
#         list.selectionModel().currentChanged.connect(self.on_current_changed)
#
#         self.horizontalLayout_1.addWidget(list)
#
#     def printItemText(self):
#         print "hello"
#
#
#     def update_locus(self):
#         repo = LocusRepository()
#
#         locus_id = str(self.LocusIdEntry.text())
#         print locus_id
#
#         locus_type = str(self.LocusTypeEntry.currentText())
#         print locus_type
#
#         sector_trench = str(self.SectorTrenchEntry.text())
#         print sector_trench
#
#         space_room = str(self.SpaceRoomEntry.text())
#         print space_room
#
#         description = str(self.DescriptionEntry.toPlainText())
#         print description
#
#         locus = Locus(locus_id, locus_type, sector_trench, space_room, description)
#
#         repo.update_locus(locus, locus_id)
#
#
#
#     def on_current_changed(self, current, previous):
#         locus_id = current.data().toString()
#
#
#         # print 'selected item index found at %s with data: %s' % (current.row(), current.data().toString())
#         repo = LocusRepository()
#
#         locus = repo.get_locus(locus_id)
#         index = self.LocusTypeEntry.findText(locus.locus_type, QtCore.Qt.MatchFixedString)
#         if index >= 0:
#             self.LocusTypeEntry.setCurrentIndex(index)
#
#         self.LocusIdEntry.setText(locus.locus_id)
#         #self.LocusTypeEntry.setItemText(2, locus.locus_type)
#         self.SpaceRoomEntry.setText(locus.space_room)
#         self.SectorTrenchEntry.setText(locus.sector_trench)
#         self.DescriptionEntry.setPlainText(locus.description)
#             # # print "coin-ui_find id is: ", coin_editable_form.Ui_Form.find_id
#             #
#             # coin_editable_form.remarks = data[0][3]
#             # # print "coin_ui.Ui_Form.remarks: ", coin_editable_form.Ui_Form.remarks
#             # # coin_ui.Ui_Form.coinweight = data.weight_gm
#             # # coin_ui.Ui_Form.cointype = data.type
#             # db.connection.commit()
#
#
#
#
#
#     def on_item_changed(self, item):
#         # If the changed item is not checked, don't bother checking others
#         # if not item.checkState():
#         #   return
#
#         # Loop through the items until you get None, which
#         # means you've passed the end of the list
#         # i = 0
#         # while model.item(i):
#         #     if not model.item(i).checkState():
#         #         return
#         #     i += 1
#         print (item)
#
#
#
#     def save_locus(self):
#
#         if self.LocusIdEntry.text() == '':
#
#             self.insert_locus()
#         else:
#             self.update_locus()
#
#
#
#     def insert_locus(self):
#         repo = LocusRepository()
#
#
#         locus_id = str(self.LocusIdEntry.text())
#         print locus_id
#         locus_type = str(self.LocusTypeEntry.currentText())
#         print locus_type
#
#         sector_trench = str(self.SectorTrenchEntry.text())
#         print sector_trench
#
#         space_room = str(self.SpaceRoomEntry.text())
#         print space_room
#
#         description = str(self.DescriptionEntry.toPlainText())
#         print description
#
#         locus = Locus(locus_id, locus_type, sector_trench, space_room, description)
#
#
#         repo.insert_locus(locus)
#
#         # if self.LocusIdEntry.text() == '':
#         #
#         #     print 'insert'
#         # else:
#         #     print 'update'
#
# # def Save_clicked(self):
# #         repo.insert_locus()
#
# # def ShowAll_clicked(self):
# #             #self.dialog.exec_()
# #         #        self.coin_edit.clicked.connect(self.editTable)
# #
# #         #self.LocusTypeEntry = self.LocusTypeEntry.currentIndexChanged.connect(self.selected)
# #         repo = LocusRepository()
# #         repo.getAllLocus()
#

def addproject(self):
    import newproject_ui
    second = newproject_ui.Ui_Form

    second.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main = AppMainwindow()

    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
