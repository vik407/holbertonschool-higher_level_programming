#!/usr/bin/python3
# Write a script that lists all states from the database hbtn_0e_0_usa


def main():
    """Get variables, connect to mysql and run the query """
    from sys import argv
    import MySQLdb

    username = str(argv[1])
    password = str(argv[2])
    db_name = str(argv[3])

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name,
                         charset="utf8")
    con = db.cursor()
    con.execute("SELECT * FROM states WHERE " +
                "name LIKE BINARY 'N%' ORDER BY 'states.id' ASC;")
    rows = con.fetchall()
    for row in rows:
        print(row)
    con.close()
    db.close()


if __name__ == '__main__':
    """Run it if main"""
    main()
