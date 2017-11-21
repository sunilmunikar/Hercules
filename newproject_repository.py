import psycopg2
import sys

from spatialiteConnection import SpatialiteDbConnect
#from sqlite3 import dbapi2 as db

class ExcavationRepository(object):
   # def __init__(self):


    def insert_excavation(self, excavation):
        self.spatialiteDbConnect = SpatialiteDbConnect()
        cursor = self.spatialiteDbConnect.connection.cursor()

        try:
            cursor.execute("INSERT  INTO  tbl_excavation ( projectTitle, projectType, projectSubType, projectSubTypeField, site, studyArea) "
                           "VALUES (?, ?, ?, ?, ?, ? )",
             (excavation.projectTitle, excavation.projectType, excavation.projectSubType, excavation.projectSubTypeField, excavation.site, excavation.studyArea, ))

            self.spatialiteDbConnect.connection.commit()

            cursor.execute('select * from tbl_excavation')
            print cursor.fetchall()

        except:
            print "cant insert", sys.exc_info()



    # def update_locus(self, locus, locus_id):
    #
    #     db = DatabaseConnection()
    #     cur = db.connection.cursor()
    #
    #     try:
    #         cur.execute("""update tbl_locus set locus_type = %s, sector_trench = %s, space_room = %s, description = %s
    #                         where id = %s""",
    #                     (locus.locus_type, locus.sector_trench, locus.space_room, locus.description, locus_id))
    #
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if db.connection is not None:
    #             db.connection.close()
#
# repo = ExcavationRepository()
# repo.insert_locus()


# tbl_excavation
