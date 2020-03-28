#!/usr/bin/python3

"""Write a script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':

    from sys import argv

    if len(argv) > 3:
        import MySQLdb

        username = argv[1]
        password = argv[2]
        db_name = argv[3]
        conn = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=db_name, charset="utf8"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
