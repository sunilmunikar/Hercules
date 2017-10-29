import sys
from PyQt4 import QtGui, QtCore

from locus_data import LocusDataEntryDialog

class LocusDetailedDialog(QtGui.QTabWidget):
    def __init__(self, parent=None):
        super(LocusDetailedDialog, self).__init__(parent)
        #QtGui.QTabWidget.__init__(self, parent)
        self.tab1 = QtGui.QWidget()
        self.tab2 = QtGui.QWidget()
        self.tab3 = QtGui.QWidget()
        self.tab4 = QtGui.QWidget()
        self.tab5 = QtGui.QWidget()


        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")
        self.addTab(self.tab5, "Tab 5")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()

    def tab1UI(self):
        self.layout = QtGui.QGridLayout(self)

        self.LocusIdEntry = QtGui.QLineEdit()

        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.LocusTypeSelect = QtGui.QComboBox()
        self.LocusSubType1Select = QtGui.QComboBox()
        self.LocusSubType2Select = QtGui.QComboBox()
        self.LocusSubType3Select = QtGui.QComboBox()

        self.SectorTrenchEntry = QtGui.QLineEdit()
        self.SpaceRoomEntry = QtGui.QLineEdit()
        self.LocusDescription = QtGui.QPlainTextEdit()
        self.LocusDescription.setFixedHeight(100)

        self.layout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.layout.addWidget(self.LocusIdEntry, 0, 1)

        self.layout.addWidget(QtGui.QLabel('Locus Type:', self), 0, 2)
        self.layout.addWidget(self.LocusTypeSelect, 0, 3, 1, 5)

        self.layout.addWidget(QtGui.QLabel('Locus SubType1:', self), 3, 2)
        self.layout.addWidget(self.LocusSubType1Select, 3, 3, 1, 5)
       # self.layout.setColumnMinimumWidth(1, 1)

        self.layout.addWidget(QtGui.QLabel('Locus SubType2:', self), 4, 2)
        self.layout.addWidget(self.LocusSubType2Select, 4, 3, 1, 5)

        self.layout.addWidget(QtGui.QLabel('Locus SubType3:', self), 5, 2)
        self.layout.addWidget(self.LocusSubType3Select, 5, 3, 1, 5)

        self.layout.addWidget(QtGui.QLabel('Sector/ Trench:', self), 7, 0)
        self.layout.addWidget(self.SectorTrenchEntry, 7, 1, 1, 1)

        self.layout.addWidget(QtGui.QLabel('Space/ Room:', self), 8, 0)
        self.layout.addWidget(self.SpaceRoomEntry, 8, 1, 1, 1)

        self.layout.addWidget(QtGui.QLabel('Description:', self), 9, 0)
        self.layout.addWidget(self.LocusDescription, 9, 1, 1, 8)

        self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.layout.addWidget(self.saveButton, 11, 3, 1, 2)
        self.layout.addWidget(self.cancelButton, 11, 5, 1, 2)
        self.layout.addWidget(self.showButton, 11, 1, 1, 2)



        '''set tab name '''
        self.setTabText(0, "Locus")
        self.tab1.setLayout(self.layout)

    def tab2UI(self):
        # layout = QtGui.QFormLayout()
        # sex = QtGui.QHBoxLayout()
        # sex.addWidget(QtGui.QRadioButton("Male"))
        # sex.addWidget(QtGui.QRadioButton("Female"))
        # layout.addRow(QtGui.QLabel("Sex"), sex)
        # layout.addRow("Date of Birth", QtGui.QLineEdit())

        self.tab2layout = QtGui.QGridLayout(self)

        self.LocusIdEntry = QtGui.QLineEdit()

        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.Compaction  = QtGui.QComboBox()#closed list
        self.Color = QtGui.QLineEdit()
        self.Composition = QtGui.QComboBox()#closed list
        self.Thickness = QtGui.QLineEdit()

        self.SpatialDistribution = QtGui.QLineEdit()
        self.Integrity = QtGui.QLineEdit()
        self.Tab2Description = QtGui.QPlainTextEdit()
        #self.Tab2Description.setFixedHeight(200)

        self.tab2layout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.tab2layout.addWidget(self.LocusIdEntry, 0, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Compaction:', self), 1, 0)
        self.tab2layout.addWidget(self.Compaction, 1, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Color:', self), 2, 0)
        self.tab2layout.addWidget(self.Color, 2, 1)
        # self.layout.setColumnMinimumWidth(1, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Composition:', self), 4, 0)
        self.tab2layout.addWidget(self.Composition, 4, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Thickness_cm:', self), 5, 0)
        self.tab2layout.addWidget(self.Thickness, 5, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Spatial Distribution:', self), 6, 0)
        self.tab2layout.addWidget(self.SpatialDistribution, 6, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Integrity :', self), 7, 0)
        self.tab2layout.addWidget(self.Integrity, 7, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Description:', self), 8, 0)
        self.tab2layout.addWidget(self.Tab2Description, 8, 1)

        self.showButton = QtGui.QPushButton('More Survey Locus', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.tab2layout.addWidget(self.saveButton, 10, 3, 1, 2)
        self.tab2layout.addWidget(self.cancelButton, 10, 5, 1, 2)
        self.tab2layout.addWidget(self.showButton, 10, 1, 1, 2)

        '''set tab name '''
        self.setTabText(1, "Locus Details")
        self.tab2.setLayout(self.tab2layout)

    def tab3UI(self):
        self.tab3layout = QtGui.QGridLayout(self)

        self.tab3LocusIdEntry = QtGui.QLineEdit()
        self.RelatedLocusId = QtGui.QLineEdit()


        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.Position = QtGui.QComboBox()  # closed list
        self.NatureRelationship = QtGui.QComboBox()  # closed list

        self.tab3layout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.tab3layout.addWidget(self.tab3LocusIdEntry, 0, 1)

        self.tab3layout.addWidget(QtGui.QLabel('Related Locus ID:', self), 0, 2)
        self.tab3layout.addWidget(self.RelatedLocusId, 0, 4)


        self.tab3layout.addWidget(QtGui.QLabel('Position:', self), 2, 0)
        self.tab3layout.addWidget(self.Position, 2, 1)

        self.tab3layout.addWidget(QtGui.QLabel('NatureRelationship:', self), 3, 0)
        self.tab3layout.addWidget(self.NatureRelationship, 3, 1)

        self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.tab3layout.addWidget(self.saveButton, 6, 3, 1, 2)
        self.tab3layout.addWidget(self.cancelButton, 6, 5, 1, 2)
        self.tab3layout.addWidget(self.showButton, 6, 1, 1, 2)

        '''set the tab name'''

        self.setTabText(2, "Related Loci")
        self.tab3.setLayout(self.tab3layout)

    def tab4UI(self):
        self.tab4layout = QtGui.QGridLayout(self)

        self.PolyLociIdEntry = QtGui.QLineEdit()
        self.LocusIdEntry = QtGui.QLineEdit()

        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.PolyLociType = QtGui.QComboBox()  # closed list
        self.Tab4DescriptionGroup = QtGui.QPlainTextEdit()
        self.Tab4MotivationGrouping = QtGui.QPlainTextEdit()


        self.tab4layout.addWidget(QtGui.QLabel('PolyLoci Id:', self), 0, 0)
        self.tab4layout.addWidget(self.PolyLociIdEntry, 0, 1)

        self.tab4layout.addWidget(QtGui.QLabel(' Locus ID:', self), 1, 0)
        self.tab4layout.addWidget(self.LocusIdEntry, 1, 1)

        self.tab4layout.addWidget(QtGui.QLabel('PolyLoci Type:', self), 2, 0)
        self.tab4layout.addWidget(self.PolyLociType, 2, 1)

        self.tab4layout.addWidget(QtGui.QLabel('Description Group:', self), 3, 0)
        self.tab4layout.addWidget(self.Tab4DescriptionGroup, 3, 1)

        self.tab4layout.addWidget(QtGui.QLabel('Motivation Grouping:', self), 4, 0)
        self.tab4layout.addWidget(self.Tab4MotivationGrouping, 4, 1)



        self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.tab4layout.addWidget(self.saveButton, 6, 3, 1, 2)
        self.tab4layout.addWidget(self.cancelButton, 6, 5, 1, 2)
        self.tab4layout.addWidget(self.showButton, 6, 1, 1, 2)



        '''set the tab name'''
        self.setTabText(3, "Poly Loci ")
        self.tab4.setLayout(self.tab4layout)

    def tab5UI(self):
        self.tab5layout = QtGui.QGridLayout(self)

        self.LocusIdEntry = QtGui.QLineEdit()
        self.face = QtGui.QLineEdit()


        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.ArchitecturalFeatures = QtGui.QComboBox()  # closed list
        self.FeaturesSubtype = QtGui.QComboBox()  # closed list
        self.FeatureID = QtGui.QLineEdit()
        self.FeatureWidth = QtGui.QLineEdit()
        self.FeatureHeight = QtGui.QLineEdit()
        self.FeatureDepth = QtGui.QLineEdit()
        self.Frame = QtGui.QComboBox() #closed list
        self.Order = QtGui.QComboBox() #closed list
        self.FrameWidth = QtGui.QLineEdit()
        self.FrameHeight = QtGui.QLineEdit()
        self.FrameDepth = QtGui.QLineEdit()
        self.DegreeCompletion = QtGui.QComboBox() #closed list
        self.DegreeUnfinishedComment = QtGui.QPlainTextEdit()
        self.TechnicalIndication = QtGui.QComboBox() #closed list
        self.SurfaceTreatment = QtGui.QComboBox() #closed list

        self.Decoration = QtGui.QComboBox() #closed list
        self.DecorationDimMaxLength = QtGui.QLineEdit()
        self.DecorationDimMaxHeight = QtGui.QLineEdit()
        self.DecorationDimMaxDepth = QtGui.QLineEdit()
        self.DecorationCompositionType = QtGui.QComboBox() #closed list
        self.ReliefType = QtGui.QComboBox() #closed list

        self.DecorationDirection = QtGui.QLineEdit() #Horizontal or Verticle
        self.DecorationComment = QtGui.QPlainTextEdit()


        self.DecorationDimMaxLength = QtGui.QLineEdit()
        self.VElevationLocation = QtGui.QPlainTextEdit()
        self.VElevationComment = QtGui.QPlainTextEdit()





















        self.Tab4DescriptionGroup = QtGui.QPlainTextEdit()
        self.Tab4MotivationGrouping = QtGui.QPlainTextEdit()

        self.tab4layout.addWidget(QtGui.QLabel('PolyLoci Id:', self), 0, 0)
        self.tab4layout.addWidget(self.PolyLociIdEntry, 0, 1)

        self.tab4layout.addWidget(QtGui.QLabel(' Locus ID:', self), 1, 0)
        self.tab4layout.addWidget(self.LocusIdEntry, 1, 1)

        self.tab4layout.addWidget(QtGui.QLabel('PolyLoci Type:', self), 2, 0)
        self.tab4layout.addWidget(self.PolyLociType, 2, 1)

        self.tab4layout.addWidget(QtGui.QLabel('Description Group:', self), 3, 0)
        self.tab4layout.addWidget(self.Tab4DescriptionGroup, 3, 1)

        self.tab4layout.addWidget(QtGui.QLabel('Motivation Grouping:', self), 4, 0)
        self.tab4layout.addWidget(self.Tab4MotivationGrouping, 4, 1)

        self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.tab4layout.addWidget(self.saveButton, 6, 3, 1, 2)
        self.tab4layout.addWidget(self.cancelButton, 6, 5, 1, 2)
        self.tab4layout.addWidget(self.showButton, 6, 1, 1, 2)

        self.setTabText(4, "Verticle Elevation  ")
        self.tab5.setLayout(layout)



# class LocusDetailedDialog(QtGui.QDialog):
#     def __init__(self, parent=None):
#         QtGui.QDialog.__init__(self, parent)
#
#         # self.locus = locus
#
#         self.setWindowTitle('Enter Detailed Locus Description')
#
#         self.layout = QtGui.QGridLayout(self)
#
#         self.LocusTypeSelect = QtGui.QComboBox(self)
#         self.LocusTypeSelect.addItems([
#             "CONCENTRATION",
#             "CORING",
#             "DOOR",
#             "FEATURE",
#             "FLOOR",
#             "FREESTANDING MONUMENT",
#             "HEATING INFRASTRUCTURE",
#             "INTERFACE",
#             "LAYER",
#             "LENZING",
#             "MAPPING",
#             "OBJECT",
#             "OBSERVATION",
#             "PROFILE",
#             "STAIR",
#             "SUPERSTRUCTURE",
#             "VERTICAL ELEVATION",
#             "WATER INFRASTRUCTURE",
#             "WINDOW",
#             "HORIZONTAL ELEVATION"])
#
#         # self.LocusTypeSelect.setCurrentIndex(self.LocusTypeSelect.count() - 1);
#         # for i in range(0, self.LocusTypeSelect.count() - 1):
#         #     if locus.type == self.LocusTypeSelect.itemText(i):
#         #         self.LocusTypeSelect.setCurrentIndex(i)
#
#         """get in automatic way from database """
#
#         self.LocusIdEntry = QtGui.QLineEdit()
#         """get it from the database, locus table """
#         self.LocusType = QtGui.QLineEdit()
#
#         self.SectorTrenchEntry = QtGui.QLineEdit()
#         self.SpaceRoomEntry = QtGui.QLineEdit()
#         self.DescriptionEntry = QtGui.QPlainTextEdit()
#
#         # SectorTrenchEntry
#
#         # SpaceRoomEntry
#
#         # DescriptionEntry
#
#
#         self.layout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
#         self.layout.addWidget(QtGui.QLabel('Select Locus Type:', self), 1, 0)
#         self.layout.addWidget(QtGui.QLabel('Sector / Trench:', self), 2, 0)
#         self.layout.addWidget(QtGui.QLabel('Space / Room: ', self), 3, 0)
#         self.layout.addWidget(QtGui.QLabel('Select Locus Type:', self), 4, 0)
#
#         # self.layout.addWidget(QtGui.QLabel('Select Locus Type', self), 0, 1, 1, 2)
#
#
#         self.layout.addWidget(self.LocusTypeSelect, 1, 1)
#
#         self.layout.addWidget(self.LocusIdEntry, 0, 1)
#         self.layout.addWidget(self.SectorTrenchEntry, 2, 1)
#         self.layout.addWidget(self.SpaceRoomEntry, 3, 1)
#         self.layout.addWidget(self.DescriptionEntry, 4, 1)
#
#         self.locusDetailedButton = QtGui.QPushButton('Locus Detail', self)
#         self.saveButton = QtGui.QPushButton('Save', self)
#         self.cancelButton = QtGui.QPushButton('Cancel', self)
#         self.layout.addWidget(self.saveButton, 7, 3, 1, 2)
#         self.layout.addWidget(self.cancelButton, 7, 5, 1, 2)
#         self.layout.addWidget(self.locusDetailedButton, 7, 1, 1, 2)
#
#         self.connect(self.okButton, QtCore.SIGNAL('clicked()'), self.ok)

# def main():
#         app = QtGui.QApplication(sys.argv)
#         ex = LocusDetailedDialog()
#         ex.show()
#         sys.exit(app.exec_())
#
# if __name__ == '__main__':
#         main()















        #
        # locus_id
        # locus_type_label
        # locus_type_id
        # locus_subtype1
        # locus_subtype2
        # locus_subtype3
        # Concentration_volume
        # Concentration_position
        # Concentration_mat_cat
        # compaction
        # color
        # composition
        # thickness_cm
        # spatial_distribution
        # integrity
        # description
        # Visibility
        # Vegetation
        # Current_land_use
        # time_spend
        # intensity
        # number_lines
        # number_finds
        # line_linewalker
        #





        # self.show(self)

