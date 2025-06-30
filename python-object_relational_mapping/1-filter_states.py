#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the given MySQL database.

Takes 3 arguments: mysql username, mysql password, and database name.
Connects to MySQL on localhost:3306 using MySQLdb.
Displays results sorted by states.id in ascending order.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
