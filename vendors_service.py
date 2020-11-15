#!/usr/bin/python
import psycopg2
from config import config


def print_id():
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT vendor_id FROM vendors;'
		cur.execute(q)
		ids = cur.fetchall()
		print('Existing IDs are: ', end='')
		for vendor_id in ids:
			print(vendor_id[0], sep=' ')
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def add_vendor(vendor_name):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id;'
		cur.execute(q, (vendor_name,))
		part_id = cur.fetchone()[0]
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def select_vendor(vendor_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT vendor_name FROM vendors WHERE vendor_id = %s;'
		cur.execute(q, (vendor_id,))
		name = cur.fetchone()[0]
		return(name)
	except (Exception, psycopg2.DatabaseError) as error:
        	print(error)
	finally:
		if conn is not None:
			conn.close()


def delete_vendor(vendor_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'DELETE FROM vendors WHERE vendor_id = %s;'
		cur.execute(q, (vendor_id,))
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

