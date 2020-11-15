#!/usr/bin/python
import psycopg2
from config import config


def print_id():
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT part_id FROM parts;'
		cur.execute(q)
		ids = cur.fetchall()
		print('Existing IDs are: ', end='')
		for part_id in ids:
			print(part_id[0], sep=' ')
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def add_part(part_name):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;'
		cur.execute(q, (part_name,))
		part_id = cur.fetchone()[0]
		conn.commit()
		return part_id
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def select_part(part_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT part_name FROM parts WHERE part_id = %s;'
		cur.execute(q, (part_id,))
		name = cur.fetchone()[0]
		return(name)
	except (Exception, psycopg2.DatabaseError) as error:
        	print(error)
	finally:
		if conn is not None:
			conn.close()


def delete_part(part_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'DELETE FROM parts WHERE part_id = %s;'
		cur.execute(q, (part_id,))
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
