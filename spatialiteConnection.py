import sys
# importing pyspatialite
#import pyspatialite
from sqlite3 import dbapi2 as db

# from pyspatialite import *

class SpatialiteDbConnect:
    #define the constructor
    def __init__(self):
        # try:
            """creating/connecting the sqlite database """

            self.connection = db.connect('SIIS_2017.sqlite')

            """creating a cursor"""

            #cursor = self.connection.cursor()
            # cursor.execute(
            #     '''INSERT  INTO  excavation  (projectID, projectTitle, projectType, projectSubType, site, studyArea)
            #         VALUES  (4, 'test', 'field', 'xx', 'ga', 'ta')''')
            #self.connection.commit()
            #
            # cursor = connection.execute('select * from excavation')
            # print cursor.fetchall()

            #self.connection.close()
        # except sqlite3.IntegrityError:
        #  print()



if __name__=='__main__':
    database_connection = SpatialiteDbConnect()