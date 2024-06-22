#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa: """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ connecting to mysql database """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    """ create a cursor object to interact with the database """
    cursor = db.cursor()

    """ select all stated ordered by id """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    """printing state"""
    for state in states:
        print(state)

    cursor.close()
    db.close()
