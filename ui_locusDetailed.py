import sys
from PyQt4 import QtGui, QtCore

# import VerticalElevation
# dir(VerticalElevation)


from locus_data import LocusDataEntryDialog
from locus.VerticalElevation.tabVE_ashlarSurfTreat_ui import *
from locus.VerticalElevation.tabVE_architectural_feature_ui import ArchitecturalFeature
from locus.ui_surveylocus import *
from locus.VerticalElevation.tabVE_material_ui import *
from locus.VerticalElevation.tabVEHE_spoila_ui import *
from locus.VerticalElevation.tabVE_ashlarSurfTreat_ui import *
from locus.VerticalElevation.tabVE_constructiontech_ui import *
from locus.VerticalElevation.tabVE_finishing_ui import *
from locus.HorizontalElevation.tabHE_superstrelement_ui import *
from locus.HorizontalElevation.tabHE_floor_ui import *
from locus.ui_inclusionslocus import *
from locus.VerticalElevation.VERepository import *


#from tab4VE_ui import *

class LocusDetailedDialog(QtGui.QTabWidget):
    def __init__(self, parent=None):
        super(LocusDetailedDialog, self).__init__(parent)
        #QtGui.QTabWidget.__init__(self, parent)
        self.tab1 = QtGui.QWidget()
        self.tab2 = QtGui.QWidget()
        self.tab3 = QtGui.QWidget()
        self.tab4 = QtGui.QWidget()
        self.tab5 = QtGui.QWidget()
        self.tab6 = QtGui.QWidget()



        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")
        self.addTab(self.tab5, "Tab 5")
        self.addTab(self.tab6, "Tab 6")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()

    def tab1UI(self):
        self.layout = QtGui.QGridLayout(self)

        self.LocusIdEntry = QtGui.QLineEdit()

        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.LocusType = QtGui.QComboBox()
        self.LocusSubType1Select = QtGui.QComboBox()
        self.LocusSubType2Select = QtGui.QComboBox()
        self.LocusSubType3Select = QtGui.QComboBox()

        self.SectorTrenchEntry = QtGui.QLineEdit()
        self.SpaceRoomEntry = QtGui.QLineEdit()
        self.LocusDescription = QtGui.QPlainTextEdit()
        self.LocusDescription.setFixedHeight(100)

        """Set the layout"""

        self.layout.addWidget(QtGui.QLabel('Locus Number:', self), 0, 0)
        self.layout.addWidget(self.LocusIdEntry, 0, 1)

        self.layout.addWidget(QtGui.QLabel('Locus Type:', self), 1, 0)
        self.layout.addWidget(self.LocusType, 1, 1,)

        self.layout.addWidget(QtGui.QLabel('Locus SubType1:', self), 2, 0)
        self.layout.addWidget(self.LocusSubType1Select, 2, 1)
       # self.layout.setColumnMinimumWidth(1, 1)


        self.layout.addWidget(QtGui.QLabel('Locus SubType2:', self), 3, 0)
        self.layout.addWidget(self.LocusSubType2Select, 3, 1)

        self.layout.addWidget(QtGui.QLabel('Locus SubType3:', self), 4, 0)
        self.layout.addWidget(self.LocusSubType3Select, 4, 1)

        self.layout.addWidget(QtGui.QLabel('Sector/ Trench:', self), 7, 0)
        self.layout.addWidget(self.SectorTrenchEntry, 7, 1, 1, 1)

        self.layout.addWidget(QtGui.QLabel('Space/ Room:', self), 8, 0)
        self.layout.addWidget(self.SpaceRoomEntry, 8, 1, 1, 1)

        self.layout.addWidget(QtGui.QLabel('Description:', self), 9, 0)
        self.layout.addWidget(self.LocusDescription, 9, 1, 1, 8)

        self.map = QtGui.QPushButton('Map', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.addButton = QtGui.QPushButton('Add New', self)

        self.layout.addWidget(self.map, 11, 0)
        self.layout.addWidget(self.saveButton, 11, 4)
        self.layout.addWidget(self.cancelButton, 11, 6)
        self.layout.addWidget(self.addButton, 11, 2)



        self.layout.setRowStretch(12, 1)
        self.layout.setRowStretch(10, 1)

        '''set tab name '''
        self.setTabText(0, "Locus")
        self.tab1.setLayout(self.layout)

    def tab2UI(self):
        self.tab2layout = QtGui.QGridLayout(self)

        self.LocusIdEntry = QtGui.QLineEdit()


        self.ConcentrationVolume = QtGui.QHBoxLayout()
        Vollengthlabel = QtGui.QLabel('Length')
        Volwidthlabel = QtGui.QLabel('Width')
        Volheightlabel = QtGui.QLabel('Height')
        Vollength = QtGui.QLineEdit()
        Vollength.setPlaceholderText('cm')
        Volwidth = QtGui.QLineEdit()
        Volwidth.setPlaceholderText('cm')
        Volheight = QtGui.QLineEdit()
        Volheight.setPlaceholderText('cm')


        self.ConcentrationVolume.addWidget(Vollengthlabel)
        self.ConcentrationVolume.addWidget(Vollength)
        self.ConcentrationVolume.addWidget(Volwidthlabel)
        self.ConcentrationVolume.addWidget(Volwidth)
        self.ConcentrationVolume.addWidget(Volheightlabel)
        self.ConcentrationVolume.addWidget(Volheight)

        self.ConcentrationPosition = QtGui.QPlainTextEdit()
        self.ConcentrationPosition.setFixedHeight(40)

        self.ConMaterialCat = QtGui.QPlainTextEdit()
        self.ConMaterialCat.setFixedHeight(40)




        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.Compaction  = QtGui.QComboBox()#closed list
        self.Color = QtGui.QLineEdit()
        self.Composition = QtGui.QComboBox()#closed list
        self.Thickness = QtGui.QLineEdit()

        self.SpatialDistribution = QtGui.QPlainTextEdit()
        self.SpatialDistribution.setFixedHeight(40)


        self.Integrity = QtGui.QLineEdit()
        self.Tab2Description = QtGui.QPlainTextEdit()
        self.Tab2Description.setFixedHeight(80)

        #self.Tab2Description.setFixedHeight(200)

        self.tab2layout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.tab2layout.addWidget(self.LocusIdEntry, 0, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Concentration Volume:', self), 1, 0)
        self.tab2layout.addLayout(self.ConcentrationVolume, 1, 1, 1, 2)

        self.tab2layout.addWidget(QtGui.QLabel('Concentration Position:', self), 3, 0)
        self.tab2layout.addWidget(self.ConcentrationPosition, 3, 1, 1, 2)

        self.tab2layout.addWidget(QtGui.QLabel('Concentration Material Category:', self), 4, 0)
        self.tab2layout.addWidget(self.ConMaterialCat, 4, 1, 1, 2)

        self.tab2layout.addWidget(QtGui.QLabel('Compaction:', self), 5, 0)
        self.tab2layout.addWidget(self.Compaction, 5, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Color:', self), 6, 0)
        self.tab2layout.addWidget(self.Color, 6, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Composition:', self), 7, 0)
        self.tab2layout.addWidget(self.Composition, 7, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Thickness_cm:', self), 8, 0)
        self.tab2layout.addWidget(self.Thickness, 8, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Spatial Distribution:', self), 9, 0)
        self.tab2layout.addWidget(self.SpatialDistribution, 9, 1, 1, 2)

        self.tab2layout.addWidget(QtGui.QLabel('Integrity :', self), 10, 0)
        self.tab2layout.addWidget(self.Integrity, 7, 1)

        self.tab2layout.addWidget(QtGui.QLabel('Description:', self), 11, 0)
        self.tab2layout.addWidget(self.Tab2Description, 11, 1, 1, 2)

        self.tab2layout.setRowStretch(12, 1)

        self.surveyButton = QtGui.QPushButton('Survey', self)
        # self.Floor.setStyleSheet("QtGui.QPushButton { background-color: blue}")
        self.surveyButton.setStyleSheet('QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
                                    ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
                                  'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')

        self.inclusionsButton = QtGui.QPushButton('Inclusions', self)
        # self.Floor.setStyleSheet("QtGui.QPushButton { background-color: blue}")
        self.inclusionsButton.setStyleSheet('QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
                                    ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
                                  'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')


        #self.surveyButton = QtGui.QPushButton('Survey Locus', self)
        #self.tab2layout.setRowStretch(15, 1)

        self.tab2layout.addWidget(self.surveyButton, 17, 0, 1, 1)
        self.connect(self.surveyButton, QtCore.SIGNAL('clicked()'), self.showSurveyLocus)

        self.tab2layout.addWidget(self.inclusionsButton, 17, 1, 1, 1)
        self.connect(self.inclusionsButton, QtCore.SIGNAL('clicked()'), self.showLocusInclusions)

        self.tab2layout.setRowStretch(16, 1)
        self.tab2layout.setRowStretch(18, 1)


        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.tab2layout.addWidget(self.saveButton, 20, 3, 1, 2)
        self.tab2layout.addWidget(self.cancelButton, 20, 5, 1, 2)


        '''set tab name '''
        self.setTabText(1, "Locus Details")
        #self.setStyleSheet('QTabBar::tab {background-color: lightgrey; color: white; border-bottom:black;}')
        #self.setStyleSheet('QTabBar::tab {background-color: rgb(255, 255, 255); border:1px solid rgb(255, 170, 255);}')

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

        self.tab3layout.setRowStretch(4, 1)

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

        self.LocusSubType1 = QtGui.QHBoxLayout()
        self.LocusSubType1.addWidget(QtGui.QRadioButton("Wall"))
        self.LocusSubType1.addWidget(QtGui.QRadioButton("Free Standing Monument"))

        self.Face = QtGui.QHBoxLayout()

        self.Face.addWidget(QtGui.QCheckBox("North"))
        self.Face.addWidget(QtGui.QCheckBox("South"))
        self.Face.addWidget(QtGui.QCheckBox("East"))
        self.Face.addWidget(QtGui.QCheckBox("West"))
        self.Face.addWidget(QtGui.QCheckBox("Top"))


        self.MaterialButton = QtGui.QPushButton('Material', self)
        # self.Floor.setStyleSheet("QtGui.QPushButton { background-color: blue}")
        self.MaterialButton.setStyleSheet('QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
                                                 ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
                                                    'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')


        self.ConstructionTechniqueButton = QtGui.QPushButton('Construction Technique', self)
        # self.Floor.setStyleSheet("QtGui.QPushButton { background-color: blue}")
        self.ConstructionTechniqueButton.setStyleSheet('QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px;'
                                                 ' font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
                                                    'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')

            #'background-color:#FFFFFF;color:#000000; padding: 6px; font: bold; border-radius: 10px;')

        SpoilaButton = QtGui.QPushButton('Spoila', self)
        SpoilaButton.setStyleSheet('QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px; font: bold; min-width: 20em; '
                                  'border-width: 2px; min-width: 10em; padding: 6px;}'
                                 'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')


            #'background-color:#FFFFFF; color:#000000; border-style: outset; border-width: 2px; border-radius: 5px; font: bold; min-width: 10em; padding: 6px;')
        # self.Spoila.setStyleSheet.pressed('backg)
        # self.Spoila.clicked.se()


        self.ArchitecturalFeatureButton = QtGui.QPushButton('Architectural Feature', self)
        # self.Floor.setStyleSheet("QtGui.QPushButton { background-color: blue}")
        #self.Architectural_featureButton.setStyleSheet(
         #   'background-color:#FFFFFF;color:#000000; padding: 6px; font: bold; border-radius: 10px;')
        self.ArchitecturalFeatureButton.setStyleSheet('QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px; '
                                                       'font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
                                                    'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')
        #('QtGui.QPushButton {background-color:#FFFFFF;color:#000000; padding: 6px; font: bold; border-radius: 10px; border-style: outset;}')
                                                       #"QtGui.QPushButton:pressed {background-color:#6d1818; color:#f9d6d6; border-style: inset;}")

        self.AshlarSurfaceTreatmentButton = QtGui.QPushButton('Ashlar Surface Treatment', self)



        self.AshlarSurfaceTreatmentButton.setStyleSheet('QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px; '
                                                       'font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
                                                    'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')

        self.FinishingButton = QtGui.QPushButton('Finishing', self)

        self.FinishingButton.setStyleSheet('QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px; '
                                                       'font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
                                                    'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')


        self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)

        self.tab5layout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.tab5layout.addWidget(self.LocusIdEntry, 0, 1, 1, 2)

        self.tab5layout.addWidget(QtGui.QLabel('Locus SubType:', self), 2, 0)
        self.tab5layout.addLayout(self.LocusSubType1, 2, 1)

        self.tab5layout.addWidget(QtGui.QLabel('Face:', self), 3, 0)
        self.tab5layout.addLayout(self.Face, 3, 1)

        self.tab5layout.setRowStretch(4, 1)

        '''Vertical elevation details button for pop up forms'''

        self.tab5layout.addWidget(QtGui.QLabel('Click on one of the following Buttons to enter Details about Vertical Elevation:', self), 5, 0, 1, 6)
        self.tab5layout.addWidget(self.MaterialButton, 6, 2, 1, 3)
        self.tab5layout.addWidget(self.ConstructionTechniqueButton, 9, 2, 1, 4)
        self.tab5layout.addWidget(self.AshlarSurfaceTreatmentButton, 10, 2, 1, 4)
        self.tab5layout.addWidget(SpoilaButton, 11, 2, 1, 3)
        self.tab5layout.addWidget(self.FinishingButton, 12, 2, 1, 3)
        self.tab5layout.addWidget(self.ArchitecturalFeatureButton, 13, 2, 1, 4)


        self.tab5layout.setRowStretch(15, 1)

        self.tab5layout.addWidget(self.saveButton, 16, 3, 1, 2)
        self.tab5layout.addWidget(self.cancelButton, 16, 5, 1, 2)
        self.tab5layout.addWidget(self.showButton, 16, 1, 1, 2)

        """connecting buttons to the pop-up- forms """

        self.connect(self.MaterialButton, QtCore.SIGNAL('clicked()'), self.showMaterial)
        self.connect(self.ConstructionTechniqueButton, QtCore.SIGNAL('clicked()'), self.showConstructionTechnique)
        self.connect(self.AshlarSurfaceTreatmentButton, QtCore.SIGNAL('clicked()'), self.showAshlarTreatment)
        self.connect(SpoilaButton, QtCore.SIGNAL('clicked()'), self.showSpoila)
        self.connect(self.FinishingButton, QtCore.SIGNAL('clicked()'), self.showFinishing)
        self.connect(self.ArchitecturalFeatureButton, QtCore.SIGNAL('clicked()'), self.showArchitecturalFeature)


        self.setTabText(4, "Vertical Elevation ")
        self.tab5.setLayout(self.tab5layout)

    def tab6UI(self):
        self.tab6layout = QtGui.QGridLayout(self)


        #form elements of horizontal elevation
        self.LocusIdEntry = QtGui.QLineEdit()
        self.LocusHESubType1 = QtGui.QHBoxLayout()
        self.LocusHESubType1.addWidget(QtGui.QRadioButton("Floor"))
        self.LocusHESubType1.addWidget(QtGui.QRadioButton("Superstructure"))

        self.Function = QtGui.QComboBox() #closed list


        self.FloorButton = QtGui.QPushButton('Floor', self)
        self.FloorButton.setStyleSheet(
            'QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px; '
            'font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
            'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')

        self.SpoilaButton = QtGui.QPushButton('Spoila', self)
        self.SpoilaButton.setStyleSheet(
            'QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px; '
            'font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
            'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')

        self.SuperstructureButton = QtGui.QPushButton('SuperStructure', self)
        self.SuperstructureButton.setStyleSheet(
            'QPushButton {background-color: #dbf0f9; color: #000000; border-radius: 10px; '
            'font: bold; min-width: 20em; border-width: 2px; min-width: 10em; padding: 6px;}'
            'QPushButton:pressed {background-color:#FFFFFF; color:#f9d6d6; border-style: inset;}')

        """set the layout"""

        #self.showButton = QtGui.QPushButton('Show', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)


        self.tab6layout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.tab6layout.addWidget(self.LocusIdEntry, 0, 1, 1, 2)

        self.tab6layout.addWidget(QtGui.QLabel('Locus Type:', self), 1, 0)
        self.tab6layout.addLayout(self.LocusHESubType1, 1, 1, 1, 2)

        self.tab6layout.addWidget(QtGui.QLabel('Function:', self), 2, 0)
        self.tab6layout.addWidget(self.Function, 2, 1, 1, 2)

        self.tab6layout.setRowStretch(3, 1)
        self.tab6layout.addWidget(QtGui.QLabel('Click on one of the following Buttons to enter Details about Horizontal Elevation:', self), 4, 0, 1, 6)


        """Add Buttons """
        self.tab6layout.addWidget(self.FloorButton, 5, 2, 1, 2)
        self.tab6layout.addWidget(self.SpoilaButton, 6, 2, 1, 2)
        self.tab6layout.addWidget(self.SuperstructureButton, 7, 2, 1, 2)
        self.tab6layout.setRowStretch(8, 1)


        self.tab6layout.addWidget(self.saveButton, 9, 3, 1, 2)
        self.tab6layout.addWidget(self.cancelButton, 9, 5, 1, 2)
        self.tab6layout.addWidget(self.showButton, 9, 1, 1, 2)

        """connecting buttons to the pop-up- forms """

        self.connect(self.FloorButton, QtCore.SIGNAL('clicked()'), self.showFloor)
        self.connect(self.SpoilaButton, QtCore.SIGNAL('clicked()'), self.showSpoila)
        self.connect(self.SuperstructureButton, QtCore.SIGNAL('clicked()'), self.showSuperstructure)

        '''set tab name '''
        self.setTabText(5, "Horizontal Elevaton ")
        self.tab6.setLayout(self.tab6layout)
        #self.tab6.setLayout(self.tab6layout)

        # class LocusDetailedDialog(QtGui.QDialog):




    def showSurveyLocus(self):
        self.surveyLocus = SurveyLocus()
        self.surveyLocus.show()

    def showLocusInclusions(self):
        self.inclusionLocus = InclusionLocus()
        self.inclusionLocus.show()


    def showMaterial(self):
        self.Material = VerticalElevationMaterial()
        self.Material.show()

    def showConstructionTechnique(self):
        self.constructionTech = ConstructionTechnique()
        self.constructionTech.show()

    def showAshlarTreatment(self):
        self.ashlarshow = VAshlarSurTreatment()
        self.ashlarshow.show()

    def showSpoila(self):
        self.spoilashow = Spoila()
        self.spoilashow.show()

    def showFinishing(self):
        self.Finishingshow = VFinishing()
        self.Finishingshow.show()

    def showArchitecturalFeature(self):
        self.archFeatureshow = ArchitecturalFeature()
        self.archFeatureshow.show()


    def showFloor(self):
        self.Floorshow = Floor()
        self.Floorshow.show()

    def showSuperstructure(self):
        self.Superstructureshow = SuperstructureElement()
        self.Superstructureshow.show()
