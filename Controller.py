#!/usr/bin/python
import psycopg2
import parts_service as p
import vendors_service as v
import vendor_parts_service as vp
import part_drawings_service as pd
from config import config

print('hello! Please, choose the table to work with. The options you have are:')
print('1: parts table', '2: vendors table', '3: vendor_parts table', '4: parts_drawings table', sep='\n')
n = int(input())
print('What do you want to do with this table?')
if n == 1:
	#parts_service
	print('1: add a row(by part name)', '2: select a row(by part id)', '3: delete a row(by part id)', sep='\n')
	n = int(input())
	if n == 1:
		print('input a name for a new part')
		name = input()
		part_id = p.add_part(name)
		print("added a part", name, 'with id:', part_id)
	elif n == 2:
		print('input an id to select from the table')
		p.print_id()
		part_id = input()
		print('The part by id', part_id, 'is', p.select_part(part_id))
	elif n == 3:
		print('input the id of the element you want to delete')
		p.print_id()
		part_id = input()
		p.delete_part(part_id)
		print('Deleted element by id', part_id, 'from the table')
		vp.delete_byPart(part_id)
	else:
		print('It seems that you have just entered an incorrect number of an operation to perform')
elif n == 2:
	#vendors_service
	print('1: add a row(by vendor name)', '2: select a row(by vendor id)', '3: delete a row(by vendor id)', sep='\n')
	n = int(input())
	if n == 1:
		print('input a name for a new vendor')
		name = input()
		vendor_id = v.add_vendor(name)
		print("added a vendor", name, 'with id:', vendor_id)
	elif n == 2:
		print('input an id to select from the table')
		v.print_id()
		vendor_id = input()
		print('The vendor by id', vendor_id, 'is', v.select_vendor(vendor_id))
	elif n == 3:
		print('input the id of the element you want to delete')
		v.print_id()
		vendor_id = input()
		v.delete_vendor(vendor_id)
		print('Deleted element by id', vendor_id, 'from the table')
		vp.delete_byVendor(vendor_id)
	else:
		print('It seems that you have just entered an incorrect number of an operation to perform')
elif n == 3:
	#vendor_parts_service
	print('1: add a row(by vendor id, part id)', '2: select a row(by vendor id)', '3: select a row(by part id)', sep='\n')
	n = int(input())
	if n == 1:
		print('Specify the parameters')
		vendor_id = input('vendor id:')
		part_id = input('part id:')
		vp.add_vendorPart(vendor_id, part_id)
		print("added a row with indents:", "vendor_id:", vendor_id, 'part_id:', part_id)
	elif n == 2:
		print('input an id to select from the table (vendor_id)')
		vp.print_idVendor()
		vendor_id = input()
		vp.select_partByVendor(vendor_id)
	elif n == 3:
		print('input an id to select from the table (part_id)')
		vp.print_idPart()
		part_id = input()
		vp.select_partByVendor(part_id)
	else:
		print('It seems that you have just entered an incorrect number of an operation to perform')
elif n == 4:
	#part_drawings_service
	print('1: add a row(by part id, path to the file, file extension)', '2: import a row to local storage(by part id, path to direction)', sep='\n')
	n = int(input())
	if n == 1:
		print('Specify the parameters')
		part_id = input('part id:')
		path_to_file = input('path to the file:')
		file_extension = input('file extension:')
		pd.write_blob(part_id, path_to_file, file_extension)
	elif n == 2:
		print('Specify the parameters')
		part_id = input('part id:')
		path_to_dir = input('path to the desired direction:')
		pd.read_blob(part_id, path_to_dir)
	else:
		print('It seems that you have just entered an incorrect number of an operation to perform')
else:
	print('It seems that you have just entered an incorrect number of a table to work with')


