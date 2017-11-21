import sys

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QWidget, QApplication
from PyQt4 import QtGui
from locus_repository import LocusRepository
from ui_locusDetailed import *
from ui_locus import *
import ui_newproject


class LocusController(Locus, LocusRepository):
    def __init__(self):
        # QWidget.__init__(self)
        super(LocusController, self).__init__()

        #self.setupUi()



        self.saveButton.clicked.connect(self.save_locus)
        # self.saveproject.clicked.connect(self.save_project)

        #self.ButtonGroupProjectType.buttonClicked['QAbstractButton *'].connect(self.ButtonClickedText)
        #self.ButtonGroupSubType.buttonClicked['QAbstractButton *'].connect(self.ButtonClickedText)
        # self.ButtonGroupFieldType.buttonClicked['QAbstractButton *'].connect(self.btngroup_clicked)


        # self.ButtonGroup.buttonClicked['int'].connect(self.btngroup_clicked)

        self.projectType = ""
        self.projectSubtype = ""

    def save_locus(self):
        self.insert_projectinfo()

    def insert_projectinfo(self):
       # locusNumber = str(self.LocusIdEntry.text())
       #  locusType = str(self.LocusType.currentText())
       #  locusSubType1 = str(self.LocusSubType1Select.currentText())
       #  locusSubType2 = str(self.LocusSubType2Select.currentText())
       #  locusSubType3 = str(self.LocusSubType3Select.currentText())
        locusType = ('layer')
        sectorTrench = str(self.SectorTrenchEntry.text())
        spaceRoom = str(self.SpaceRoomEntry.text())
        description = str(self.LocusDescription.toPlainText())

        newlocus = Locus(locusType, sectorTrench, spaceRoom, description)


        # newlocus = Locus(locusType, locusSubType1, locusSubType2, locusSubType3, sectorTrench, spaceRoom, description )
        repo = LocusRepository()
        repo.insert_locus(newlocus)

    # def btngroup_clicked(self, button):
    #     if button == self.ButtonGroupProjectType:
    #     # print('{0} was clicked'.format(button_or_id.text()))
    #
    #         self.projectType = button.text()
    #
    #     elif button == self.ButtonGroupSubType:
    #         self.projectSubtype = button.text()

        #         print('"Id {}" was clicked'.format(button_or_id))


    # @pyqtSlot(QtGui.QAbstractButton)
    # @pyqtSlot(int)
    # def btngroup_clicked(self, button_or_id):
    #     # print button_or_id.text() + " is selected"
    #     # self.projectType = button_or_id.text()
    #
    #     if isinstance(button_or_id, QtGui.QAbstractButton):
    #         print('{0} was clicked'.format(button_or_id.text()))
    #     elif isinstance(button_or_id, int):
    #         print('"Id {}" was clicked'.format(button_or_id))


    #     #return buttonText
    #
    # if b.text() == "Button1":
    #     if b.isChecked() == True:
    #         print b.text() + " is selected"
    #     else:
    #         print b.text() + " is deselected"
    #
    # if b.text() == "Button2":
    #     if b.isChecked() == True:
    #         print b.text() + " is selected"
    #     else:
    #         print b.text() + " is deselected"

    #
    # def projecttypeClickedText(self, Button):
    #
    #     #if self.ButtonGroupProjectType.button(int) == True:
    #         self.projectType = Button.text()
    #     else:
    #         print 'not selected '
    #     print buttonText


    def ButtonClickedText(self, Button):
        if Button == self.ButtonGroupProjectType.checkedButton():
            self.projectType = "{0}".format(Button.text(), Button)
           # print "{0}".format(Button.text(), Button)

        elif Button == self.ButtonGroupSubType.checkedButton():
            self.projectSubtype = "{0}".format(Button.text(), Button)
            #print "{0}".format(Button.text(), Button)


class Locus:
    # def __init__(self,  locusType, locusSubType1, locusSubType2, locusSubType3, sectorTrench, spaceRoom, description ):
        #self.projectID = projectID
        # self.excavation = excavation
    def __init__(self, locusType, sectorTrench, spaceRoom, description):
        #
        self.locusType = locusType
        # self.locusSubType1 = locusSubType1
        # self.locusSubType2 = locusSubType2
        # self.locusSubType3 = locusSubType3
        self.sectorTrench = sectorTrench
        self.spaceRoom = spaceRoom
        self.description = description


        #self.date = date


def main():
    app = QApplication(sys.argv)
    main = LocusControl()

    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()