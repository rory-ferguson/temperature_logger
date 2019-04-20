import sqlite3

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

	return None


def write(database, temp):
	""" Log entry to the database
		:param database: database object
		:param temp: temperature reading
		:return: id of commited row
	"""
	c = database.cursor()
	c.execute("INSERT INTO temps values(datetime('now'), (?))", (temp,))
	database.commit()
	return c.lastrowid


def close(database):
	""" Closes the database connection
		:param database: database object
	"""	
	database.close()


def main():
	conn = connect('temperatue.db')
	write(conn, "22")
	close(conn)


if __name__ == '__main__':
	main()
