import sqlite3
import sys
import os



def connect(database):
	""" Connect to database
		:param database: database name
		:return: conn
	"""
	try:
		conn = sqlite3.connect(database)
		return conn
	except Exception as e:
		print(e)

	return None


def main():
	conn = connect('temperature.db')
	print(conn)


if __name__ == '__main__':
	main()