#!/usr/bin/python3
"""Display all states matching the given name safely using parameterized queries."""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (searched,))
    states = cursor.fetchall()
    for state in states:
        print(state)
cursor.close()
db.close()
