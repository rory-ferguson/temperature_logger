import sqlite3
import sys


def connect(database):
    """ Create a connection to a database
        :param database: database name
        :return: conn
    """
    try:
        conn = sqlite3.connect(database)
        return conn
    except Exception as e:
        print(e)
        sys.exit()

    return None


def write(database, temp):
    """ Log entry to the database
        :param database: database object
        :param temp: temperature reading
        :return: id of commited row
        :rtype: int
    """
    c = database.cursor()
    try:
        c.execute("INSERT INTO temps values(datetime('now', 'localtime'), (?))", (temp,))
    except Exception as e:
        print(e)
            
    database.commit()
    return c.lastrowid
    


def close(database):
    """ Closes the database connection
        :param database: database object
    """
    database.close()


def main():
    conn = connect('temperature.db')
    write(conn, "22")
    close(conn)


if __name__ == '__main__':
    main()

