#!/usr/bin/env python
# map function for matrix multiply
#Input file assumed to have lines of the form "A,i,j,x", where i is the row index, j is the column index, and x is the value in row i, column j of A. Entries of A are followed by lines of the form "B,i,j,x" for the matrix B. 
#It is assumed that the matrix dimensions are such that the product A*B exists. 

#Input arguments:
#m should be set to the number of rows in A, p should be set to the number of columns in B.
 
import sys
import string
import numpy

#number of rows in A
m = int(sys.argv[1]) 

#number of columns in B
p = int(sys.argv[2])


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
  #Remove leading and trailing whitespace
  line = line.strip()

  #Split line into array of entry data
  entry = line.split(",")
    
  # Set row, column, and value for this entry
  row = int(entry[1])
  col = int(entry[2])
  value = float(entry[3])

  #If this is an entry in matrix A...
  if (entry[0] == "A"):
		
    #Generate the necessary key-value pairs
    for k in range(p):
      print('{0:d},{1:d}\tA,{2:d},{3:f}'.format(row, k, col, value))

  #Otherwise, if this is an entry in matrix B...
  else:
		
    #Generate the necessary key-value pairs
    for k in range(m):
      print('{0:d},{1:d}\tB,{2:d},{3:f}'.format(k, col, row, value))

	
        
