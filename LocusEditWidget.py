import sys
from PyQt4 import QtGui as qtGui
from PyQt4 import QtCore as qtCore

import psycopg2 as mdb

# from PyQt4.QtGui import *
from PyQt4.QtGui import QTabWidget

import coin_ui
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

        self.resultsTable.setSortingEnabled(True)
