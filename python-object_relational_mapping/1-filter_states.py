#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the given MySQL database.

Takes 3 arguments: mysql username, mysql password, and database name.
Connects to MySQL on localhost:3306 using MySQLdb.
Displays results sorted by states.id in ascending order.
"""
import sys
import MySQLdb


def get_filtered_states(username, password, db_name):

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name, charset="utf8")

    cursor = db.cursor()

    # Select states where name starts with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    get_filtered_states(sys.argv[1], sys.argv[2], sys.argv[3])
