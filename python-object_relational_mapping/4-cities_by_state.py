#!/usr/bin/python3
"""Display all values in the states table where name matches the argument."""
import MySQLdb
import sys


def main():
    """Define the main function"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name"
                   " FROM cities"
                   " JOIN states ON cities.state_id = states.id"
                   " ORDER BY cities.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
