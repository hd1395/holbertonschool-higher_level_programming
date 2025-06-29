#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

Connects to MySQL server using MySQLdb and retrieves states
ordered by their id in ascending order.
"""

import MySQLdb
import sys


def list_states(username, password, dbname):
    """
    Connects to MySQL database and prints all states sorted by id.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        dbname (str): database name
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=dbname
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
