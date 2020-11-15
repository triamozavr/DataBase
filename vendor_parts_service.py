#!/usr/bin/python
import psycopg2
from config import config


def print_idPart():
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT part_id FROM vendor_parts;'
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


def print_idVendor():
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT vendor_id FROM vendor_parts;'
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


def add_vendorPart(vendor_id, part_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)'
		cur.execute(q, (vendor_id, part_id))
		conn.commit(),
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def select_partByVendor(vendor_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT part_id FROM vendor_parts WHERE vendor_id = %s;'
		cur.execute(q, (vendor_id,))
		names = cur.fetchall()
		print('Parts for vendor by id', vendor_id, 'are:')
		for name in names:
			print(name[0])
	except (Exception, psycopg2.DatabaseError) as error:
        	print(error)
	finally:
		if conn is not None:
			conn.close()


def select_vendorByPart(part_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'SELECT vendor_id FROM vendor_parts WHERE part_id = %s;'
		cur.execute(q, (part_id,))
		names = cur.fetchall()
		print('Vendors for part by id', part_id, 'are:')
		for name in names:
			print(name[0])
	except (Exception, psycopg2.DatabaseError) as error:
        	print(error)
	finally:
		if conn is not None:
			conn.close()


def delete_byVendor(vendor_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'DELETE FROM vendor_parts WHERE vendor_id = %s;'
		cur.execute(q, (vendor_id,))
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


def delete_byPart(part_id):
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		q = 'DELETE FROM vendor_parts WHERE part_id = %s;'
		cur.execute(q, (part_id,))
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn._close()
