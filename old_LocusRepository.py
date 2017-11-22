import psycopg2
import sys

from postgresConnection import DatabaseConnection
import Locus_entry_ui


# cur = db.connection.cursor()

class LocusRepository:
    def get_locus(self, locus_id):
        try:
            db = DatabaseConnection()
            cur = db.connection.cursor()
            cur.execute("""select * from tbl_locus WHERE id = %s""", [str(locus_id)])
            locus = cur.fetchall()

            return Locus(locus[0][0], locus[0][1], locus[0][2], locus[0][3], locus[0][4])
            db.connection.close()

        except psycopg2.Error, e:
            # print "Error %d: %s" % (e.args[0], e.args[1])
            print e
            # return result

    def get_all_locus(self):

        try:
            db = DatabaseConnection()
            cur = db.connection.cursor()
            cur.execute("""SELECT * FROM tbl_locus""")
            result = cur.fetchall()

            locus_list = []
            for locus in result:
                locus_list.append(
                    # Locus(locus[0], locus[1], locus[2], locus[3], locus[4], locus[5], locus[6], locus[7], locus[8]))
                    Locus(locus[0], locus[1], locus[2], locus[3], locus[4]))

        except psycopg2.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return locus_list

    def insert_locus(self, locus):
        db = DatabaseConnection()
        cur = db.connection.cursor()

        try:
            cur.execute("""INSERT  INTO  tbl_locus  (id, locus_type, sector_trench, space_room, description)
                        VALUES(%s, %s, %s, %s, %s)""",
                        (locus.locus_id, locus.locus_type, locus.sector_trench, locus.space_room, locus.description))

        except:
            print "cant insert", sys.exc_info()

    def update_locus(self, locus, locus_id):

        db = DatabaseConnection()
        cur = db.connection.cursor()

        try:
            cur.execute("""update tbl_locus set locus_type = %s, sector_trench = %s, space_room = %s, description = %s 
                            where id = %s""",
                        (locus.locus_type, locus.sector_trench, locus.space_room, locus.description, locus_id))

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if db.connection is not None:
                db.connection.close()


# tbl_locus
class Locus:
    def __init__(self, locus_id, locus_type, sector_trench, space_room,
                 description):
        self.locus_id = locus_id
        # self.excavation = excavation
        # self.year = year
        # self.site = site
        # self.locus_number = locus_number
        self.locus_type = locus_type
        self.sector_trench = sector_trench
        self.space_room = space_room
        self.description = description
