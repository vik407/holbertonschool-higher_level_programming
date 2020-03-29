#!/usr/bin/python3
# Write a script that lists all cities from the database hbtn_0e_4_usa


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
    con.execute("SELECT cities.name FROM cities " +
                "JOIN states ON cities.state_id = states.id " +
                "WHERE states.name = %s ORDER BY cities.id ASC", (st_name,))
    rows = con.fetchall()
    print(", ".join([row[0] for row in rows]))
    con.close()
    db.close()


if __name__ == '__main__':
    """Run it if main"""
    main()
