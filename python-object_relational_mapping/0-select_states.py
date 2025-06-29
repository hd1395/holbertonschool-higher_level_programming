#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

def list_state(username, password, dbname):
  """
    Connects to MySQL database and prints all states sorted by id.

    Args:
        username: MySQL username
        password: MySQL password
        dbname: database name
    """
    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=username,
      passwd=password,
      db=dbname
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
    
