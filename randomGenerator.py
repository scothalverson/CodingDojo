#!/usr/bin/python

'''
Syntax:  
	./randomGenerator.py <rows> <columns> <outfile>
where:
	<rows> is a positive integer specifying the number of rows in the output file
	<columns> is a positive integer specifying the number of columns in the output file
	<outfile> is a the (ascii text) file to which the data will written
'''
import random
import numpy as np
import sys

nx = 10
ny = 10
filename = 'life.txt'
type = 'random'

if len(sys.argv) >= 3:
	nx = int(sys.argv[1])
	ny = int(sys.argv[2])
if len(sys.argv) >= 4:
	filename = sys.argv[3]
if len(sys.argv) >= 5:
	type = sys.argv[4]

array = []

if type == 'random':

	for i in xrange(ny):
		array.append(np.random.randint(2, size=nx))

with open(filename,'w') as f:
	f.write(str(nx) + ' ' + str(ny) + '\n')
	for i in array:
		for j in i:
			f.write(str(j))
		f.write('\n')
		

