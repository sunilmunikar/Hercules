import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection


class ConstructionTechnique(QtGui.QWidget):
    def __init__(self):
        super(ConstructionTechnique, self).__init__()

        self.gridlayout = QtGui.QGridLayout()

        self.LocusIdEntry = QtGui.QLineEdit()
        #self.Face = QtGui.QLineEdit()
        self.ID = QtGui.QLineEdit()  # combination of locusID + face

        '''combo box later to be replaced from the datatype from the spatialite database'''
       # self.ConstructionTechnique = QtGui.QComboBox()  # closed list
        self.ConstructionType = QtGui.QComboBox()  # closed list
        self.ConstructionID = QtGui.QLineEdit()
        #self.AshlarMasonryGeom = QtGui.QComboBox()  # closed list
        self.ConstructionSubtype = QtGui.QComboBox()  # closed list
        self.NumColumns = QtGui.QLineEdit()
        self.DisColumnsAxes = QtGui.QLineEdit()

        '''Average Dimensions in cm'''

        self.Length = QtGui.QLineEdit()
        self.Length.setPlaceholderText('in cm')
        self.Height = QtGui.QLineEdit()
        self.Height.setPlaceholderText('in cm')
        self.Width = QtGui.QLineEdit()
        self.Width.setPlaceholderText('in cm')


       # self.Bond = QtGui.QComboBox()  # closed list
        self.CoursesNum = QtGui.QLineEdit()
        self.CoursesHeight = QtGui.QLineEdit()

        self.CoursesArtDeco = QtGui.QHBoxLayout()
        self.CoursesArtDeco.addWidget(QtGui.QRadioButton("Yes"))
        self.CoursesArtDeco.addWidget(QtGui.QRadioButton("No"))


        self.CoursesDecoNum = QtGui.QLineEdit()
        self.CourseDecoComment = QtGui.QPlainTextEdit()

        self.Joints = QtGui.QHBoxLayout()
        self.Joints.addWidget(QtGui.QRadioButton("Dry"))
        self.Joints.addWidget(QtGui.QRadioButton("Mortared"))

        self.ConstructionTechnique = QtGui.QHBoxLayout()
        self.ConstructionTechnique.addWidget(QtGui.QCheckBox("Masonry"))
        self.ConstructionTechnique.addWidget(QtGui.QCheckBox("Colonnade"))
        self.ConstructionTechnique.addWidget(QtGui.QCheckBox("Bedrock"))
        self.ConstructionTechnique.addWidget(QtGui.QCheckBox("Other"))

        self.AshlarMasonryGeom = QtGui.QHBoxLayout()
        self.AshlarMasonryGeom.addWidget(QtGui.QCheckBox("Polygonal"))
        self.AshlarMasonryGeom.addWidget(QtGui.QCheckBox("Trapezoidal"))
        self.AshlarMasonryGeom.addWidget(QtGui.QCheckBox("Rectangular"))
        self.AshlarMasonryGeom.addWidget(QtGui.QCheckBox("Other"))

        self.Bond = QtGui.QHBoxLayout()
        self.Bond.addWidget(QtGui.QCheckBox("Strecher"))
        self.Bond.addWidget(QtGui.QCheckBox("Header-strecher"))
        self.Bond.addWidget(QtGui.QCheckBox("Other"))



        '''Mortar   Dimensions in cm'''

        self.MortaredThickness = QtGui.QLineEdit()
        self.MortaredThickness.setPlaceholderText('in mm')

        self.MortaredWidth = QtGui.QLineEdit()
        self.MortaredWidth.setPlaceholderText('in mm')


        self.SurfTreatPCourse = QtGui.QLineEdit()

        self.RubblePortionHeight = QtGui.QLineEdit()
        self.RubblePortionHeight.setPlaceholderText('in cm')


        self.BrickCoursesBond = QtGui.QLineEdit()
        self.BrickCoursesNum = QtGui.QLineEdit()
        self.BrickCoursesJointThick = QtGui.QLineEdit()
        self.BrickCoursesJointThick.setPlaceholderText('in cm')

        self.BrickCoursesJointWidth = QtGui.QLineEdit()
        self.BrickCoursesJointWidth.setPlaceholderText('in cm')

        self.GeneralComment = QtGui.QPlainTextEdit()


        '''Grid layout settings for a form '''

        self.gridlayout.addWidget(QtGui.QLabel('Locus Id:', self), 0, 0)
        self.gridlayout.addWidget(self.LocusIdEntry, 0, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' ID', self), 1, 0)
        self.gridlayout.addWidget(self.ID, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Construction Technique:', self), 2, 0)
        self.gridlayout.addLayout(self.ConstructionTechnique, 2, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Construction Type:', self), 3, 0)
        self.gridlayout.addWidget(self.ConstructionType, 3, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Construction Subtype:', self), 3, 3)
        self.gridlayout.addWidget(self.ConstructionSubtype, 3, 4, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Ashlar Masonary Geometry:', self), 4, 0)
        self.gridlayout.addLayout(self.AshlarMasonryGeom, 4, 1, 1, 2)


        self.gridlayout.addWidget(QtGui.QLabel(' Number Columns:', self), 5, 0)
        self.gridlayout.addWidget(self.NumColumns, 5, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Distance Columns Axes:', self), 5, 2)
        self.gridlayout.addWidget(self.DisColumnsAxes, 5, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Length:', self), 7, 0)
        self.gridlayout.addWidget(self.Length, 7, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Height :', self), 7, 2)
        self.gridlayout.addWidget(self.Height, 7, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Width:', self), 7, 4)
        self.gridlayout.addWidget(self.Width, 7, 5)

        self.gridlayout.addWidget(QtGui.QLabel('Bond:', self), 8, 0)
        self.gridlayout.addLayout(self.Bond, 8, 1)

        #self.gridlayout.addWidget(QtGui.QLabel('Bond:', self), 8, 0)
        #self.gridlayout.addLayout(self.AvgDimension, 9, 1)

        self.gridlayout.addWidget(QtGui.QLabel(' Courses Number', self), 10, 0)
        self.gridlayout.addWidget(self.CoursesNum, 10, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Courses Height:', self), 10, 2)
        self.gridlayout.addWidget(self.CoursesHeight, 10, 3)

        self.gridlayout.addWidget(QtGui.QLabel('Courses Art Decoration:', self), 11, 0)
        self.gridlayout.addLayout(self.CoursesArtDeco, 11, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Courses Decoration Number:', self), 12, 0)
        self.gridlayout.addWidget(self.CoursesDecoNum, 12, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Courses Decoration Comment', self), 13, 0)
        self.gridlayout.addWidget(self.CourseDecoComment, 13, 1, 1, 2)

        self.gridlayout.addWidget(QtGui.QLabel('Joints:', self), 14, 0)
        self.gridlayout.addLayout(self.Joints, 14, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Mortared Thickess:', self), 15, 0) #in mm
        self.gridlayout.addWidget(self.MortaredThickness, 15, 1, 1, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Mortared Width:', self), 15, 2)  # cm
        self.gridlayout.addWidget(self.MortaredWidth, 15, 3)

        self.gridlayout.addWidget(QtGui.QLabel(' Surface Treatment/Course:', self), 16, 0)  # cm
        self.gridlayout.addWidget(self.SurfTreatPCourse, 16, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Rubble Portion Height:', self), 17, 0)  # cm
        self.gridlayout.addWidget(self.RubblePortionHeight, 17, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Brick Course Bond:', self), 18, 0)
        self.gridlayout.addWidget(self.BrickCoursesBond, 18, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Brick Courses Joint Thickness:', self), 19, 0)
        self.gridlayout.addWidget(self.BrickCoursesJointThick, 19, 1)

        self.gridlayout.addWidget(QtGui.QLabel('Brick Courses Joint Width:', self), 19, 2)
        self.gridlayout.addWidget(self.BrickCoursesJointWidth, 19, 3 )

        self.gridlayout.addWidget(QtGui.QLabel('General Comment:', self), 20, 0)
        self.gridlayout.addWidget(self.GeneralComment, 20, 1, 1, 2)

        self.gridlayout.setRowStretch(21, 1)


        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.gridlayout.addWidget(self.saveButton, 22, 3, 1, 2)
        self.gridlayout.addWidget(self.cancelButton, 22, 5, 1, 2)
       # self.gridlayout.addWidget(self.showButton, 15, 1, 1, 2)

        self.setLayout(self.gridlayout)
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Vertical Elevation: Construction Technique ')
# #
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main = ConstructionTechnique()
#     main.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()
