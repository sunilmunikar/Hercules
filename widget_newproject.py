import sys
from PyQt4 import QtCore

from PyQt4.QtGui import QListView, QWidget, QApplication, QStandardItemModel, QStandardItem, QLabel
from newproject_repository import ExcavationRepository
from  spatialiteConnection import SpatialiteDbConnect
import ui_newproject


class Form(QWidget, ui_newproject.NewProject):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        #self.setupUi(self)

        self.saveproject.clicked.connect(self.save_project)



        #self.saveproject.clicked.connect(self.save_project)


    def save_project(self):
        self.insert_projectinfo()



    def insert_projectinfo(self):

        projectTitle = str(self.ProjectTitle.text())
        print projectTitle

        # ui.b1.stateChanged.connect(lambda: repo.btngroup(self.b1))
        # ui.b2.stateChanged.connect(lambda: repo.btngroup(self.b2))
        #projectType = self.ButtonGroup.buttonClicked.connect(lambda: self.buttonclickedText(self.ButtonGroup))
        projectType = self.ButtonGroup.buttonClicked['QAbstractButton *'].connect(self.btngroup)


        print projectType

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

    def btngroup(self, btn):
        print btn.text() + " is selected"


    # def buttonclickedText(self, Button):
    #     buttonText = Button.text()
    #     print buttonText
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



def main():
    app = QApplication(sys.argv)
    main = Form()

    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
