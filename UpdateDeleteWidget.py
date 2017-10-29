import sys
from PyQt4 import QtGui as qtGui
from PyQt4 import QtCore as qtCore

import psycopg2 as mdb

# from PyQt4.QtGui import *
from PyQt4.QtGui import QTabWidget

#import coin_ui
from postgresConnection import DatabaseConnection

# import the ui file
#import coin_ui
#from app import coin


# declare Variables
db = DatabaseConnection()
myCursor = db.connection.cursor()


class UpdateDelete(qtGui.QWidget):
    def __init__(self, parent=None):
        super(UpdateDelete, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.topLabel = qtGui.QLabel("Below are your users/tasks")
        self.resultsTable = qtGui.QTableWidget()
        self.populateButton = qtGui.QPushButton('Populate')
        self.populateButton.clicked.connect(self.populate)

        self.grid = qtGui.QGridLayout()
        self.grid.setSpacing(5)

        self.grid.addWidget(self.resultsTable)
        self.grid.addWidget(self.populateButton)

        self.setLayout(self.grid)
        self.resultsTable.setEditTriggers(qtGui.QAbstractItemView.AllEditTriggers)

    def handleEditbutton(self, find_id):

        find_id_tbl = self.resultsTable.item(find_id, 0).text()
        find_id_tbl = str(find_id_tbl)
        print find_id_tbl

        try:
            myCursor.execute("""SELECT * FROM coin where find_id = %s;""", [find_id_tbl])

            #myCursor.execute("""SELECT * FROM coin where find_id ='SA-2018';""")
            data = myCursor.fetchall()

            #mapping the data from the table to the line form


            coin_editable_form = app.Coin()
            coin_editable_form.find_id = data[0][0]
            #print "coin-ui_find id is: ", coin_editable_form.Ui_Form.find_id

            coin_editable_form.remarks = data[0][3]
            #print "coin_ui.Ui_Form.remarks: ", coin_editable_form.Ui_Form.remarks
            #coin_ui.Ui_Form.coinweight = data.weight_gm
            # coin_ui.Ui_Form.cointype = data.type
            db.connection.commit()

        except mdb.Error, e:
            print e.message

        tabs = QTabWidget()
        tabs.addTab(coin_editable_form, "Update")

        tabs.setGeometry(450, 100, 400, 520)
        tabs.setWindowTitle('CoinTableEdit')
        tabs.show()

    def updateCoin(self, table_index):
        find_id_tbl = self.resultsTable.item(table_index, 0).text()
        find_id_tbl = str(find_id_tbl)
        print find_id_tbl
        #app.coin.show()
        try:
            myCursor.execute("""update coin set find_id = %s where find_id = %s""", [find_id_tbl])
            #myCursor.execute("""SELECT * FROM coin where find_id ='SA-2018';""")
            data = myCursor.fetchall()

            #mapping the data from the table to the line form

            coin_editable_form = app.Coin()
            coin_editable_form.Ui_Form.find_id = data[0][0]
            print "coin-ui_find id is: ", coin_editable_form.Ui_Form.find_id

            coin_editable_form.Ui_Form.coinweight = data[0][3]
            print "coin_ui.Ui_Form.: ", coin_editable_form.Ui_Form.coinweight
            db.connection.commit()

            print "Total number of rows updated :", myCursor.rowcount

            myCursor.execute("""SELECT * FROM coin""")
            rows = myCursor.fetchall()
            for row in rows:
                print "find_id = ", row[0]
                print "weight_gm = ", row[2], "\n"
            print "operation done successfully"

            db.connection.close()
            # self.resultsTable

        except mdb.Error, e:
            print e.message

    def notifyMe(self, index):
        print index

    def populate(self):
        try:
            myCursor.execute("""SELECT COUNT(*) FROM coin""")
            result = myCursor.fetchall()
            for row in result:
                numOfrows = row[0]

        except mdb.Error, e:

            print "Error %d: %s" % (e.args[0], e.args[1])

            # sys.exit(1)

        headerDict = ["find_id", "type", "weight_gm ", "remarks", "action"]
        nrows, ncols = numOfrows, len(headerDict)
        self.resultsTable.setSortingEnabled(False)
        self.resultsTable.setRowCount(nrows)
        self.resultsTable.setColumnCount(ncols)

        for index in range(len(headerDict)):
            self.resultsTable.setHorizontalHeaderItem(index, qtGui.QTableWidgetItem(headerDict[index]))

        try:
            myCursor.execute("""SELECT * FROM coin""")
            result = myCursor.fetchall()
            self.btn = []

            for i in range(nrows):
                for j in range(ncols):
                    if j == 4:
                        self.btn.append(i)
                        self.btn[i] = qtGui.QPushButton(self)
                        self.btn[i].setGeometry(qtCore.QRect(0, 100 + (([i][0]) * 20), 100, 20))
                        self.btn[i].setText('edit'.format([i][0]))

                        self.resultsTable.setCellWidget(i, j, self.btn[i])
                        self.btn[i].clicked.connect(lambda checked, x=i: self.handleEditbutton(x))

                    else:
                        item = qtGui.QTableWidgetItem('%s' % (result[i][j]))
                        item.setFlags(qtCore.Qt.ItemIsEnabled)
                        self.resultsTable.setItem(i, j, item)

        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)

        self.resultsTable.setSortingEnabled(True)
