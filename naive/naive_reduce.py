#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values
current_key = None
current_res = 0.0
value_dict = dict()

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

  #Remove leading and trailing whitespace
  line = line.strip()
    
  #Get key/value
  key, value = line.split('\t',1)
  
  #Parse key/value input
  try:
    row, col = map(int, key.split(','))
    value = value.split(',')
    key = (row, col)
    replicate_key, element_value = int(value[1]), float(value[2])
  except:
    continue

  #If we are still on the same key...
  if key == current_key:
    
    #Process key/value pair
    if replicate_key not in value_dict:
      value_dict[replicate_key] = [element_value]
    else:
      value_dict[replicate_key].append(element_value)

  #Otherwise, if this is a new key...
  else:
    
    #If this is a new key and not the first key we've seen
    if current_key:
      
      #compute/output result to STDOUT
      for j in range(n):
        if (j in value_dict) and (len(value_dict[j]) == 2):
          current_res += value_dict[j][0] * value_dict[j][1]
      print ('({0:d},{1:d}),{2:f}'.format(row, col, current_res))
  
    current_key = key
    value_dict = dict()
    
    #Process input for new key
    value_dict[replicate_key] = [element_value]
    current_res = 0.0


#Compute/output result for the last key 

if current_key:
  for j in range(n):
    if (j in value_dict) and (len(value_dict[j]) == 2):
      current_res += value_dict[j][0] * value_dict[j][1]
  print('({0:d},{1:d}),{2:f}'.format(row, col, current_res))



