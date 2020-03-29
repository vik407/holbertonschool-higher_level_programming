#!/usr/bin/python3
# Write a script that takes in an argument and displays all values in the
# states table of hbtn_0e_0_usa where name matches the argument.


def main():
    """Get variables, connect to mysql and run the query """
    from sys import argv
    import MySQLdb

    username = str(argv[1])
    password = str(argv[2])
    db_name = str(argv[3])
    st_name = str(argv[4])

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name,
                         charset="utf8")
    con = db.cursor()
    con.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC;",
                (st_name,))
    rows = con.fetchall()
    for row in rows:
        print(row)
    con.close()
    db.close()


if __name__ == '__main__':
    """Run it if main"""
    main()
