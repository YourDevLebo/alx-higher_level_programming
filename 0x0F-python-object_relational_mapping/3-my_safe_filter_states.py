#!/usr/bin/python3
# takes four argv safe from mysql injection

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state = sys.argv[4]

    database = MySQLdb.Connect(user=username,
                               passwd=password,
                               db=database_name,
                               port=3306)
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC;",
                (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    database.close()
