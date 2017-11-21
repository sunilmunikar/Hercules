import sys
from PyQt4 import QtCore
from PyQt4 import QtSql




def checkQSQLITE():
    result = QtSql.QSqlDatabase.isDriverAvailable('QSQLITE')
    print("Sqlite{}".format(result))
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE", "sqlite")
    cname = db.connectionName()
    print("db.connectionName() = ", cname)
    print("db.lastError:", db.lastError().text())
    result = db.open()
    print("Datenbank  {}".format(result))
    db.close()
    if result:
        if db.isOpen():
            print("Datenbank konnte nicht geschlossen werden.")
            print("db.lastError:", db.lastError().text())
        else:
            print("Datenbank geschlossen.")
    QtSql.QSqlDatabase.removeDatabase(cname)


if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv[1:])

    dbliste = QtSql.QSqlDatabase.drivers()
    print(dbliste)
    print("-----")
    #checkQPSQL()
    print("-----")
    checkQSQLITE()
