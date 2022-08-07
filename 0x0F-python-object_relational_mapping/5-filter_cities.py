#!/usr/bin/python3

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(f"SELECT cities.name \
                  FROM cities \
                  INNER JOIN states ON states.id = cities.state_id \
                  WHERE states.name = %s \
                  ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()
    print(", ".join(cities[0] for cities in rows))
    cur.close()
    db.close()
