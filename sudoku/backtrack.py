#!/usr/bin/env python
# encoding: utf-8
"""
backtrack.py

Learn how to use the backtrack method

Created by Christopher Woodall on 2010-12-26.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

def main():
	asa = [[0,0,3],[3,2,1],[2,1,0]]
	rows = asa
	cols = [[0,3,2],[0,2,1],[3,1,0]]
	asa_new = []
	
	row = 0
	for a in asa:
		column = 0
		for item in a:
			if item == 0:
				p = True
				while p:
					item += 1
					if not item in (set(rows[row]) or set(cols[column])):
						asa_new.append(item)
						p = False
			else:
				asa_new.append(item)
			column += 1
		row +=1
	print asa_new
		
if __name__ == '__main__':
	main()

