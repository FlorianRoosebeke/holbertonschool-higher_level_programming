#!/usr/bin/python3
"""script that takes in the name of a state as an argument
 and lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def main():
    """Define the main function"""
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities"
                   " JOIN states ON cities.state_id = states.id"
                   " WHERE states.name = %s"
                   " ORDER BY cities.id ASC", (state,))
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
