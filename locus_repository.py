import psycopg2
import sys

from spatialiteConnection import SpatialiteDbConnect
from sqlite3 import dbapi2 as db

class LocusRepository(object):
   # def __init__(self):


    def insert_locus(self, locus):
        self.spatialiteDbConnect = SpatialiteDbConnect()
        cursor = self.spatialiteDbConnect.connection.cursor()

        try:
            # cursor.execute("INSERT  INTO  tbl_locus ( locusNumber, locusType, locusSubType1, locusSubType2, locusSubType3 sectorTrench, sectorRoom, descripton) "
            #                "VALUES (?, ?, ?, ?, ?, ?, ?, ? )",
            #  (locus.locusType, locus.locusSubType1, locus.locusSubType2, locus.locusSubType3, locus.sectorTrench, locus.spaceRoom, locus.descripton, ))

            cursor.execute(
                "INSERT  INTO  tbl_locus(locusType, sectorTrench, sectorRoom, description) "
                "VALUES (?, ?, ?, ? )",
                (locus.locusType, locus.sectorTrench, locus.spaceRoom, locus.description,))

            self.spatialiteDbConnect.connection.commit()

            cursor.execute('select * from tbl_locus')
            print cursor.fetchall()

        except:
            print "cant insert", sys.exc_info()







