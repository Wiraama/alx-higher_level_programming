#!/usr/bin/python3
""" list all states with 'N' in database """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ connect to mysql """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    """ create cursor object """
    cursor = db.cursor()

    """SELECTING ALL states """
    cursor.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id""")

    states = cursor.fetchall()
    printed_states = set()
    for state in states:
        """if state[1] not in printed_states:
            print(state)
            printed_states.add(state[1])"""
        print(state)
    cursor.close()
    db.close()
