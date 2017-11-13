import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection



class Spoila(QtGui.QWidget):
    def __init__(self):
        super(Spoila, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.LocusIdEntry = QtGui.QLineEdit()
        self.SpoilaID = QtGui.QLineEdit() #locusid+dace+spoilaid

        '''dimension of Spoila '''
        self.Length = QtGui.QLineEdit()
        self.Length.setPlaceholderText('in cm')

        self.Height = QtGui.QLineEdit()
        self.Height.setPlaceholderText('in cm')

        self.Width = QtGui.QLineEdit()
        self.Width.setPlaceholderText('in cm')


        self.IdenSpoilaComment = QtGui.QPlainTextEdit()
        self.ArchContextLocationComment = QtGui.QPlainTextEdit()

        self.Location = QtGui.QLineEdit()
        self.CourseNum = QtGui.QLineEdit() #same as in construction technique

        self.SpoilaPosition = QtGui.QHBoxLayout()
        self.SpoilaPosition.addWidget(QtGui.QCheckBox("Vertical"))
        self.SpoilaPosition.addWidget(QtGui.QCheckBox("Horizontal"))
        self.SpoilaPosition.addWidget(QtGui.QCheckBox("Upside Down"))

        self.Epigraphy = QtGui.QLineEdit()

        self.OriVisible = QtGui.QHBoxLayout()
        self.OriVisible.addWidget(QtGui.QRadioButton("Yes"))
        self.OriVisible.addWidget(QtGui.QRadioButton("No"))


        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.TechnicalIndication = QtGui.QComboBox()  # closed list
        self.SurfaceTreatment = QtGui.QComboBox()  # closed list
        self.FeatureID = QtGui.QLineEdit()

        self.Decoration = QtGui.QHBoxLayout()
        self.Decoration.addWidget(QtGui.QCheckBox("Undecorated"))
        self.Decoration.addWidget(QtGui.QCheckBox("Decorated Individual"))
        self.Decoration.addWidget(QtGui.QCheckBox("Decorated Individual"))

        """Decoration Dimension """
        self.DecorationDimMaxLength = QtGui.QLineEdit()
        self.DecorationDimMaxLength.setPlaceholderText('in cm')

        self.DecorationDimMaxHeight = QtGui.QLineEdit()
        self.DecorationDimMaxHeight.setPlaceholderText('in cm')

        self.DecorationDimMaxDepth = QtGui.QLineEdit()
        self.DecorationDimMaxDepth.setPlaceholderText('in cm')

        self.DecorationDimMaxProj = QtGui.QLineEdit()
        self.DecorationDimMaxProj.setPlaceholderText('in cm')


        self.DecorationCompositionType = QtGui.QHBoxLayout()
        self.DecorationCompositionType.addWidget(QtGui.QCheckBox("Sequence"))
        self.DecorationCompositionType.addWidget(QtGui.QCheckBox("Band"))
        self.DecorationCompositionType.addWidget(QtGui.QCheckBox("Scroll"))

        self.DecorationDirection = QtGui.QHBoxLayout()
        self.DecorationDirection.addWidget(QtGui.QRadioButton("Horizontal"))
        self.DecorationDirection.addWidget(QtGui.QRadioButton("Vertical"))

        self.DecorationComment = QtGui.QPlainTextEdit()
        self.SpoilaGeneralComment = QtGui.QPlainTextEdit()


        """positioning in the layour"""



        self.gridlayout.addWidget(QtGui.QLabel('Locus Id:', self), 0, 0)
        self.gridlayout.addWidget(self.LocusIdEntry, 0, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Spoila Id:', self), 0, 3)
        self.gridlayout.addWidget(self.SpoilaID, 0, 4, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Length:', self), 1, 0)
        self.gridlayout.addWidget(self.Length, 1, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Height', self), 1, 2)
        self.gridlayout.addWidget(self.Height, 1, 3, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Width:', self), 1, 4)
        self.gridlayout.addWidget(self.Width, 1, 5, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Identification Comment :', self), 2, 0)
        self.gridlayout.addWidget(self.IdenSpoilaComment, 2, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Architectural Context Location Comment :', self), 3, 0)
        self.gridlayout.addWidget(self.ArchContextLocationComment, 3, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Location:', self), 4, 0)
        self.gridlayout.addWidget(self.Location, 4, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Course Number', self), 5, 0)
        self.gridlayout.addWidget(self.CourseNum, 5, 1, 1, 1) # also in construction technique

        self.gridlayout.addWidget(QtGui.QLabel('Spoila position :', self), 6, 0)
        self.gridlayout.addLayout(self.SpoilaPosition, 6, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Epigraphy:', self), 7, 0)
        self.gridlayout.addWidget(self.Epigraphy, 7, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Originally Visible:', self), 8, 0)
        self.gridlayout.addLayout(self.OriVisible, 8, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Technical Indication ', self), 9, 0)
        self.gridlayout.addWidget(self.TechnicalIndication, 9, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Surface Treatment:', self), 9, 2)
        self.gridlayout.addWidget(self.SurfaceTreatment, 9, 3, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Feature Id:', self), 10, 0)
        self.gridlayout.addWidget(self.FeatureID, 10, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Decoration:', self), 11, 0)
        self.gridlayout.addLayout(self.Decoration, 11, 1)

        self.gridlayout.addWidget(QtGui.QLabel('DecoDimMaxLength:', self), 12, 0) #cm
        self.gridlayout.addWidget(self.DecorationDimMaxLength, 12, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' DecoDimMaxHeight:', self), 12, 2) #cm
        self.gridlayout.addWidget(self.DecorationDimMaxHeight, 12, 3, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('DecoDimMaxDepth:', self), 12, 4) #cm
        self.gridlayout.addWidget(self.DecorationDimMaxDepth, 12, 5, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('DecoDimMaxProj:', self), 13, 0) #cm
        self.gridlayout.addWidget(self.DecorationDimMaxProj, 13, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Decoration Composition Type:', self), 14, 0)
        self.gridlayout.addLayout(self.DecorationCompositionType, 14, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Decoration Direction:', self), 15, 0)
        self.gridlayout.addLayout(self.DecorationDirection, 15, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Decoration Comment', self), 16, 0)
        self.gridlayout.addWidget(self.DecorationComment, 16, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Spoila Comment:', self), 17, 0)
        self.gridlayout.addWidget(self.SpoilaGeneralComment, 17, 1, 1, 2)
        self.gridlayout.setRowStretch(19, 1)

        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.gridlayout.addWidget(self.saveButton, 20, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 20, 5, 1, 2)

        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Vertical Elevation: Spoila')



#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = Spoila()
#
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
