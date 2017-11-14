
# importing pyspatialite
#import pyspatialite
from sqlite3 import dbapi2 as db


class SpatialiteDbConnect:
    #define the constructor
    def __init__(self):
        try:
            # creating/connecting the test_db

            connection = db.connect('SIIS_2017.sqlite')

            #creating a cursor

            cursor = connection.execute('SELECT  sqlite_version()')
            print cursor.fetchall()


            #exception
        except:
            pprint("I am unable to connect to the database.")

if __name__=='__main__':
    database_connection = SpatialiteDbConnect()