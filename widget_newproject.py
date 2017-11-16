import sys

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QWidget, QApplication
from PyQt4 import QtGui
from newproject_repository import ExcavationRepository
import ui_newproject

class NewprojectControl(QWidget, ui_newproject.NewProject):
    def __init__(self):
        # QWidget.__init__(self)
        super(NewprojectControl, self).__init__()

        self.setupUi()

        self.saveproject.clicked.connect(self.save_project)
        #self.saveproject.clicked.connect(self.save_project)

        self.ButtonGroupProjectType.buttonClicked['QAbstractButton *'].connect(self.ButtonClickedText)
        self.ButtonGroupSubType.buttonClicked['QAbstractButton *'].connect(self.ButtonClickedText)
        #self.ButtonGroupFieldType.buttonClicked['QAbstractButton *'].connect(self.btngroup_clicked)


        # self.ButtonGroup.buttonClicked['int'].connect(self.btngroup_clicked)

        self.projectType = ""
        self.projectSubtype = ""

    def save_project(self):
        self.insert_projectinfo()

    def insert_projectinfo(self):
        projectTitle = str(self.ProjectTitle.text())
        #print projectTitle

        projectType = self.projectType
        #print projectType

        projectSubType = self.projectSubtype
        #print projectSubType



        # ui.b1.stateChanged.connect(lambda: repo.btngroup(self.b1))
        # ui.b2.stateChanged.connect(lambda: repo.btngroup(self.b2))
        #projectType = self.ButtonGroup.buttonClicked.connect(lambda: self.buttonclickedText(self.ButtonGroup))

        # ui.ProjectType = str(self.LocusTypeEntry.currentText())
        # print locus_type
        #
        # sector_trench = str(self.SectorTrenchEntry.text())
        # print sector_trench
        #
        # space_room = str(self.SpaceRoomEntry.text())
        # print space_room
        #
        # description = str(self.DescriptionEntry.toPlainText())
        # print description

        #newexcavation = Excavation(projectTitle, 'ff', 'fd', 'ss', 'fd')
        repo = ExcavationRepository()
        repo.insert_excavation(projectTitle)

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




def main():
    app = QApplication(sys.argv)
    main = NewprojectControl()

    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()