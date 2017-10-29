import sys
import psycopg2
from pprint import pprint

#Define DatabaseConnection class in python file to connect to Postgres database through psycopg2 python module.
class DatabaseConnection:
    #define the constructor
    def __init__(self):
        try:
            self.connection=psycopg2.connect(
                "dbname='test' user='postgres' password='postgres' host= 'localhost' port='5433'" )
            self.connection.autocommit = True
            cur =self.connection.cursor()
            #exception
        except:
            pprint("I am unable to connect to the database.")

if __name__=='__main__':
    database_connection = DatabaseConnection()