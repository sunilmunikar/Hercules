
# importing pyspatialite
#import pyspatialite
from sqlite3 import dbapi2 as db


class SpatialiteDbConnect:
    #define the constructor
    def __init__(self):
        try:
            # creating/connecting the test_db

            connection = db.connect('SIIS_2017.sqlite')
            #cursor = connection.cursor()
            #db.autocommit(True)

            #creating a cursor

            #cursor = connection.execute('SELECT  sqlite_version()')

            # """cursor = connection.execute(
            #     """INSERT  INTO  excavation  ( projectTitle, projectType, projectSubType, site, studyArea)
            #      VALUES (?, ?, ?, ?, ? )""", ('ann', 'bbb', 'c', 'd', 'e'))"""
            #
            cursor = connection.execute('SELECT * FROM  excavation')

            print cursor.fetchall()


            #connection.close()



            #exception
        except:
            print("I am unable to connect to the database.")

if __name__=='__main__':
    database_connection = SpatialiteDbConnect()