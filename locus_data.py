import sys
from PyQt4 import QtGui, QtCore

import psycopg2 as mdb
from postgresConnection import DatabaseConnection
#from locusDetailed import *

db = DatabaseConnection()
cur = db.connection.cursor()

class LocusDataEntryDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

#        self.locus = locus

        self.setWindowTitle('Enter Locus Data')

        self.layout = QtGui.QGridLayout(self)




       # self.LocusTypeSelect = QtGui.QComboBox(self)
        #self.LocusSubType1Select = QtGui.QComboBox(self)
        # self.LocusSubType2Select = QtGui.QComboBox(self)
        # self.LocusSubType3Select = QtGui.QComboBox(self)


        # def getlocustype(self):
        #     try:
        #         cur.execute("""SELECT * FROM tbl_locus_type""")
        #         resultsTable = cur.fetchall()
        #
        #         self.locusType_db = []
        #
        #         for row in resultsTable:
        #             #self.locusType_db
        #            # id = row['label'][1]
        #             label = row[1][1]
        #            # self.locusType_db = [id, label]
        #         #print id
        #             #print label
        #             #print self.locusType_db
        #             self.locusType_db.append(resultsTable(row, 1))
        #         print resultsTable[1][1]
        #         print self.locusType_db
        #
        #     except mdb.Error, e:
        #         print "Error %d: %s" % (e.args[0], e.args[1])
















                # self.locusType_db = dict([('CONCENTRATION', 1), ('CORING', 2)])
        #

        #self.LocusTypeSelected = self.LocusTypeSelect.currentIndexChanged.connect(self.LocusTypeSelected)



        # self.LocusTypeSelect.setCurrentIndex(self.LocusTypeSelect.count() - 1);
        # for i in range(0, self.LocusTypeSelect.count() - 1):
        #     # if locus.type == self.LocusTypeSelect.itemText(i):
        #        self.LocusTypeSelect.setCurrentIndex(i)
        #
        #     print self.LocusTypeSelect.current.item(i)




        self.LocusIdEntry = QtGui.QLineEdit()

        '''combo box later to be replaced from the datatype from the spatialite database'''
        self.LocusTypeSelect = QtGui.QComboBox()
        self.LocusSubType1Select = QtGui.QComboBox()
        self.LocusSubType2Select = QtGui.QComboBox()
        self.LocusSubType3Select = QtGui.QComboBox()




        self.SectorTrenchEntry = QtGui.QLineEdit()
        self.SpaceRoomEntry = QtGui.QLineEdit()
        self.LocusDescription = QtGui.QPlainTextEdit()




        self.layout.addWidget(QtGui.QLabel('Locus ID:', self), 0, 0)
        self.layout.addWidget(self.LocusIdEntry, 0, 1)



        self.layout.addWidget(QtGui.QLabel('Select Locus Type:', self), 2, 0)
        self.layout.addWidget(self.LocusTypeSelect, 2, 1, 1, 3)

        self.layout.addWidget(QtGui.QLabel('Select Locus SubType1:', self), 2, 4)
        self.layout.addWidget(self.LocusSubType1Select, 2, 5, 1, 4)

        self.layout.addWidget(QtGui.QLabel('Select Locus SubType2:', self), 5, 0)
        self.layout.addWidget(self.LocusSubType2Select, 5, 1, 1, 3)

        self.layout.addWidget(QtGui.QLabel('Select Locus SubType3:', self), 5, 4)
        self.layout.addWidget(self.LocusSubType3Select, 5, 5, 1, 4)

        self.layout.addWidget(QtGui.QLabel('Description:', self), 7, 0)
        self.layout.addWidget(self.LocusDescription, 8, 1, 1, 4)














        # self.layout.addWidget(QtGui.QLabel('Sector / Trench:', self), 2, 0)
        # self.layout.addWidget(QtGui.QLabel('Space / Room: ', self), 3, 0)
        # self.layout.addWidget(QtGui.QLabel('Select Locus Type:', self), 4, 0)
        #
        #self.layout.addWidget(QtGui.QLabel('Select Locus Type', self), 0, 1, 1, 2)
        #
        #
        #
        #
        # self.layout.addWidget(self.SectorTrenchEntry, 2, 1)
        # self.layout.addWidget(self.SpaceRoomEntry, 3, 1)
        # self.layout.addWidget(self.DescriptionEntry, 4, 1)


        self.locusDetailedButton = QtGui.QPushButton('Locus Detailed', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.cancelButton = QtGui.QPushButton('Cancel', self)
        self.layout.addWidget(self.saveButton, 9, 3, 1, 2)
        self.layout.addWidget(self.cancelButton, 9, 5, 1, 2)
        self.layout.addWidget(self.locusDetailedButton, 9, 1, 1, 2)

       # self.connect(self.okButton, QtCore.SIGNAL('clicked()'), self.ok)


    # def LocusTypeSelected(self):
    #     # try:
    #     #     cur.execute("""SELECT COUNT(*) FROM tbl_locus """)
    #     #
    #     #     # myCursor.execute("""SELECT * FROM coin where find_id ='SA-2018';""")
    #     #     self.resultsTable = cur.fetchall()
    #     #     for row in self.resultsTable:
    #     #         numOfrows = row[0]
    #     #
    #     # except mdb.Error, e:
    #     #
    #     #     print "Error %d: %s" % (e.args[0], e.args[1])
    #     #
    #     # nrows = numOfrows
    #     # self.resultsTable.setRowCount(nrows)
    #     # headerDict = ["id", "label"]
    #     # nrows, ncols = numOfrows, len(headerDict)
    #     # self.resultsTable.setColumnCount(ncols)
    #     #
    #     # # for index in range(len(headerDict)):
    #     # # self.resultsTable.setHorizontalHeaderItem(index, QtGui.QTableWidgetItem(headerDict[index]))
    #     #
    #     # try:
    #     #     cur.execute("""SELECT * FROM tbl_locus""")
    #     #     resultsTable = cur.fetchall()
    #     #     self.locusType_db = []
    #     #
    #     #     for i in range(nrows):
    #     #         self.locusType = resultsTable([i][0])
    #     #         print self.locusType
    #     #         self.LocusTypeSelect.addItems(self.locusType)
    #     #
    #     #         # self.locusType_db[] = dict([(resultsTable[1]), resultsTable[0])
    #     #
    #     #         # self.LocusTypeSelect.addItems(self.locusTypeId(row[0]))
    #     #
    #     # except mdb.Error, e:
    #     #     print e.message
    #
    #     self.selectedLocusType = self.LocusTypeSelect.currentText()
    #
    #     #self.locusType_db.fromkeys[self.selectedLocusType];
    #
    #     self.LocusSubType1Select.addItems(self.dictionary_locustype[self.selectedLocusType])
    #
    #     # try:
    #     #     cur.execute("""SELECT * FROM tbl_locus_subtype1 ;""")
    #     #
    #     #     # myCursor.execute("""SELECT * FROM coin where find_id ='SA-2018';""")
    #     #     data = cur.fetchall()
    #     #     data.show()
    #     #     locusType_dict = []
    #     #     #
    #     #     # for row in data:
    #     #     #     if self.selectedLocusType == data.label

       # self.locusDetailedButton.clicked.connect(locusdetailed)
        self.connect(self.locusDetailedButton, QtCore.SIGNAL('clicked()'), self.locusdetailed)


    def locusdetailed(self):
        detailedshow = LocusDetailedDialog(self)
        detailedshow.show()


    def subType1Selected(self):
        self.selectedSubType1 = self.LocusSubType1Select.currentText()
        self.subType1Select.addItems(self.dictionary_locustype[self.selectedSubType1])



