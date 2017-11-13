import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection



class SurveyLocus(QtGui.QWidget):
    def __init__(self):
        super(SurveyLocus, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.Toponame = QtGui.QLineEdit()
        self.CollectionUnit = QtGui.QHBoxLayout()
        self.CollectionUnit.addWidget(QtGui.QCheckBox("Grid"))
        self.CollectionUnit.addWidget(QtGui.QCheckBox("Lines"))
        self.CollectionUnit.addWidget(QtGui.QCheckBox("Graph"))
        self.Chronology = QtGui.QLineEdit()



        self.Visibility = QtGui.QLineEdit()
        self.Visibility.setPlaceholderText('ranges from 1-5')
        self.Vegetation = QtGui.QLineEdit()
        self.TimeSpend = QtGui.QLineEdit()
        self.Intensity = QtGui.QLineEdit()
        self.NoOfCollectionUnit = QtGui.QLineEdit()
        self.NoOfCollectionUnit.setPlaceholderText('ranges from 1-20')
        self.NoOfFinds = QtGui.QLineEdit()
        self.NoOfFinds.setPlaceholderText('ranges from 1-50')
        self.CurrentLandUse = QtGui.QComboBox()  # closed list : Agriculture, fallow, forest,  other


        self.gridlayout.addWidget(QtGui.QLabel('TopoName:', self), 0, 0)
        self.gridlayout.addWidget(self.Toponame, 0, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Collection Unit:', self), 1, 0)
        self.gridlayout.addLayout(self.CollectionUnit, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Visibility:', self), 2, 0)
        self.gridlayout.addWidget(self.Visibility, 2, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Vegetation:', self), 3, 0)
        self.gridlayout.addWidget(self.Vegetation, 3, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Current Land use:', self), 4, 0)
        self.gridlayout.addWidget(self.CurrentLandUse, 4, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Time Spend:', self), 5, 0)
        self.gridlayout.addWidget(self.TimeSpend, 5, 1)


        self.gridlayout.addWidget(QtGui.QLabel('Intensity:', self), 6, 0)
        self.gridlayout.addWidget(self.Intensity, 6, 1)


        self.gridlayout.addWidget(QtGui.QLabel('Number of Collection Unit:', self), 7, 0)
        self.gridlayout.addWidget(self.NoOfCollectionUnit, 7, 1)


        self.gridlayout.addWidget(QtGui.QLabel('Number of Finds:', self), 8, 0)
        self.gridlayout.addWidget(self.NoOfFinds, 8, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Chronology:', self), 9, 0)
        self.gridlayout.addWidget(self.Chronology, 9, 1)

        self.gridlayout.setRowStretch(10, 1)

       # self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.gridlayout.addWidget(self.saveButton, 15, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 15, 5, 1, 2)
        #self.gridlayout.addWidget(self.showButton, 15, 1, 1, 2)

        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Locus Survey Details')




def main():
    app = QtGui.QApplication(sys.argv)
    main = SurveyLocus()

    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
