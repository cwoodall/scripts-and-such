#!/usr/bin/env python

def count_ones(a_byte):
	"""
	count_ones(a_byte) : Counts the number of 1 bits in the input byte a byte
	returns number_of_ones which is the number of bytes in a_byte
	"""
	val = 0
	# loop until there are no more 1s
	while a_byte > 0:
		# if a_byte is odd then there is a 1 in the 1st bit
		if a_byte % 2 > 0:
			val += 1

		# shift the byte one to the right
		a_byte = a_byte >> 1

	return val

print(count_ones(0b101)) # 2
print(count_ones(1982)) # 9
