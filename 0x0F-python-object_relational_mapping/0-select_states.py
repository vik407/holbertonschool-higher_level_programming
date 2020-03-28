#!/usr/bin/python3
# Write a script that lists all states from the database hbtn_0e_0_usa

import sys
import MySQLdb

if __name__ == '__main__':
    mysql_usr = sys.argv[1]
    mysql_psw = sys.argv[2]
    mysql_db = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_usr,
                         passwd=mysql_psw,
                         db=mysql_db,
                         charset="utf8")

    conn = db.cursor()
    conn.execute("SELECT * FROM states ORDER BY id ASC")
    rows = conn.fetchall()
    for row in rows:
        print(row)
    conn.close()
    db.close()
