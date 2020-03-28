#!/usr/bin/python3
# Write a script that lists all states from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv


def main():
    """Get variables, connect to mysql and run the query """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8")
    con = db.cursor()
    con.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = con.fetchall()
    for row in rows:
        print(row)
    con.close()
    db.close()


if __name__ == '__main__':
    """Run it if main"""
    main()
