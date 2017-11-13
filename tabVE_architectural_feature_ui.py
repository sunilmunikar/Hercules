import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection



class ArchitecturalFeature(QtGui.QWidget):
    def __init__(self):
        super(ArchitecturalFeature, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.LocusIdEntry = QtGui.QLineEdit()
        self.Face = QtGui.QLineEdit()


        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.ArchitecturalFeatures = QtGui.QComboBox()  # closed list
        self.FeaturesSubtype = QtGui.QComboBox()  # closed list
        self.FeatureID = QtGui.QLineEdit()
        """dimension """
        self.FeatureWidth = QtGui.QLineEdit()
        self.FeatureWidth.setPlaceholderText('in cm')
        self.FeatureHeight = QtGui.QLineEdit()
        self.FeatureHeight.setPlaceholderText('in cm')
        self.FeatureDepth = QtGui.QLineEdit()
        self.FeatureDepth.setPlaceholderText('in cm')

        self.Frame = QtGui.QComboBox() #closed list
        self.Order = QtGui.QComboBox() #closed list

        self.FrameWidth = QtGui.QLineEdit()
        self.FrameWidth.setPlaceholderText('in cm')

        self.FrameHeight = QtGui.QLineEdit()
        self.FrameHeight.setPlaceholderText('in cm')

        self.FrameDepth = QtGui.QLineEdit()
        self.FrameDepth.setPlaceholderText('in cm')

        self.DegreeCompletion = QtGui.QComboBox() #closed list
        self.DegreeUnfinishedComment = QtGui.QPlainTextEdit()
        self.TechnicalIndication = QtGui.QComboBox() #closed list
        self.SurfaceTreatment = QtGui.QComboBox() #closed list

       # self.Decoration = QtGui.QComboBox() #closed list
        self.Decoration = QtGui.QHBoxLayout()
        self.Decoration.addWidget(QtGui.QCheckBox("Undecorated"))
        self.Decoration.addWidget(QtGui.QCheckBox("Decorated Individual"))
        self.Decoration.addWidget(QtGui.QCheckBox("Decorated Individual"))

        self.DecorationDimMaxLength = QtGui.QLineEdit()
        self.DecorationDimMaxLength.setPlaceholderText('in cm')

        self.DecorationDimMaxHeight = QtGui.QLineEdit()
        self.DecorationDimMaxHeight.setPlaceholderText('in cm')

        self.DecorationDimMaxDepth = QtGui.QLineEdit()
        self.DecorationDimMaxDepth.setPlaceholderText('in cm')

        self.DecorationDimMaxProj = QtGui.QLineEdit()
        self.DecorationDimMaxProj.setPlaceholderText('in cm')

        #self.DecorationCompositionType = QtGui.QComboBox() #closed list
        self.DecorationCompositionType = QtGui.QHBoxLayout()
        self.DecorationCompositionType.addWidget(QtGui.QCheckBox("Sequence"))
        self.DecorationCompositionType.addWidget(QtGui.QCheckBox("Band"))
        self.DecorationCompositionType.addWidget(QtGui.QCheckBox("Scroll"))



        self.ReliefType = QtGui.QComboBox() #closed list

        #self.DecorationDirection = QtGui.QLineEdit() #Horizontal or Verticle
        self.DecorationDirection = QtGui.QHBoxLayout()
        self.DecorationDirection.addWidget(QtGui.QRadioButton("Horizontal"))
        self.DecorationDirection.addWidget(QtGui.QRadioButton("Vertical"))

        self.DecorationComment = QtGui.QPlainTextEdit()

        self.VElevationLocation = QtGui.QLineEdit()
        self.VElevationComment = QtGui.QPlainTextEdit()


        self.gridlayout.addWidget(QtGui.QLabel('Locus Id:', self), 0, 0)
        self.gridlayout.addWidget(self.LocusIdEntry, 0, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Face', self), 0, 3)
        self.gridlayout.addWidget(self.Face, 0, 4)

        self.gridlayout.addWidget(QtGui.QLabel('Architectural Features:', self), 1, 0)
        self.gridlayout.addWidget(self.ArchitecturalFeatures, 1, 1, 1, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Feature ID:', self), 2, 0) #locus id + Face
        self.gridlayout.addWidget(self.FeatureID, 2, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Features Subtype:', self), 2, 3)
        self.gridlayout.addWidget(self.FeaturesSubtype, 2, 4)

        self.gridlayout.addWidget(QtGui.QLabel('Feature Width:', self), 3, 0)
        self.gridlayout.addWidget(self.FeatureWidth, 3, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Feature Height', self), 3, 2)
        self.gridlayout.addWidget(self.FeatureHeight, 3, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Feature Depth', self), 3, 4)
        self.gridlayout.addWidget(self.FeatureDepth, 3, 5)

        self.gridlayout.addWidget(QtGui.QLabel('Enter the information about Frame:', self), 4, 0, 1, 4)

        self.gridlayout.addWidget(QtGui.QLabel('Frame :', self), 5, 0)
        self.gridlayout.addWidget(self.Frame, 5, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Order:', self), 5, 3)
        self.gridlayout.addWidget(self.Order, 5, 4, 1, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Frame Width:', self), 6, 0)
        self.gridlayout.addWidget(self.FrameWidth, 6, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Frame Height', self), 6, 2)
        self.gridlayout.addWidget(self.FrameHeight, 6, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Frame Depth:', self), 6, 4)
        self.gridlayout.addWidget(self.FrameDepth, 6, 5)

        self.gridlayout.addWidget(QtGui.QLabel('Degree Completion:', self), 7, 0)
        self.gridlayout.addWidget(self.DegreeCompletion, 7, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Degree Unfinished Comment:', self), 7, 3, 1, 4)
        self.gridlayout.addWidget(self.DegreeUnfinishedComment, 7, 4, 1, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Technical Indication:', self), 8, 0)
        self.gridlayout.addWidget(self.TechnicalIndication, 8, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Surface Treatment:', self), 9, 0)
        self.gridlayout.addWidget(self.SurfaceTreatment, 9, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Enter the information Decoration:', self), 10, 0, 1, 4)

        self.gridlayout.addWidget(QtGui.QLabel('Decoration:', self), 11, 0)
        self.gridlayout.addLayout(self.Decoration, 11, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('DecoDimMax Length:', self), 12, 0) #cm
        self.gridlayout.addWidget(self.DecorationDimMaxLength, 12, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' DecoDimMax Height:', self), 12, 2) #cm
        self.gridlayout.addWidget(self.DecorationDimMaxHeight, 12, 3)

        self.gridlayout.addWidget(QtGui.QLabel('DecoDimMax Depth:', self), 12, 4) #cm
        self.gridlayout.addWidget(self.DecorationDimMaxDepth, 12, 5)

        self.gridlayout.addWidget(QtGui.QLabel('DecoDimMax Projection:', self), 13, 0) #cm
        self.gridlayout.addWidget(self.DecorationDimMaxProj, 13, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Decoration Composition Type:', self), 14, 0)
        self.gridlayout.addLayout(self.DecorationCompositionType, 14, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Relief Type:', self), 15, 0)
        self.gridlayout.addWidget(self.ReliefType, 15, 1)


        self.gridlayout.addWidget(QtGui.QLabel('Decoration Direction:', self), 16, 0)
        self.gridlayout.addLayout(self.DecorationDirection, 16, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Decoration Comment', self), 16, 3)
        self.gridlayout.addWidget(self.DecorationComment, 16, 4)

        self.gridlayout.addWidget(QtGui.QLabel('VerticalElevation Location:', self), 17, 0)
        self.gridlayout.addWidget(self.VElevationLocation, 17, 1)

        self.gridlayout.addWidget(QtGui.QLabel('VerticalElevation Comment:', self), 17, 3)
        self.gridlayout.addWidget(self.VElevationComment, 17, 4)

        self.gridlayout.setRowStretch(19, 1)



       # self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.gridlayout.addWidget(self.saveButton, 20, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 20, 5, 1, 2)
        #self.gridlayout.addWidget(self.showButton, 20, 1, 1, 2)

        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Vertical Elevation Architectural Feature')




# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = ArchitecturalFeature()
#
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
