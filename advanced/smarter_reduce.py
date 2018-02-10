#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
import numpy

A_BLOCK_SCALE = 20
B_BLOCK_SCALE = 20

#number of columns of A/rows of B
n = int(sys.argv[1])


# compute/output result to STDOUT

def CalculateElementMultiResult(current_key, a_value, b_value):
  # load block number
  a_block, b_block = current_key[0], current_key[1]
  # the range of index which involving calculation
  min_i = A_BLOCK_SCALE * a_block
  max_i = min(A_BLOCK_SCALE * (1+a_block) - 1, i_scale)
  min_k = B_BLOCK_SCALE * b_block
  max_k = min(B_BLOCK_SCALE * (1+b_block) - 1, k_scale)
  # compute/output result
  for i1 in range(max_i - min_i + 1):
    for k1 in range(max_k - min_k + 1):
      i = min_i + i1
      k = min_k + k1
      current_res = 0
      for j in range(n):
        current_res += a_value[i][j] * b_value[j][k]
      print('({0:d},{1:d}),{2:f}'.format(i, k, current_res))


#Process input of matrix A

def StoreDataToA(matrix, row, col, a_value, i_scale):
  if row not in a_value:
    a_value[row] = dict()
  a_value[row][col] = val
  i_scale = max(i_scale, row) # range of index
  return a_value, i_scale


#Process input of matrix B

def StoreDataToB(matrix, row, col, b_value, k_scale):
  if row not in b_value:
    b_value[row] = dict()
  b_value[row][col] = val
  k_scale = max(k_scale, col) # range of index
  return b_value, k_scale



#Create data structures to hold the current row/column values
current_key = None
current_res = 0
a_value, b_value = dict(), dict()
i_scale, k_scale = 0, 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

  #Remove leading and trailing whitespace
  line = line.strip()
    
  #Get key/value
  key, value = line.split('\t',1)
  
  #Parse key/value input
  try:
    key = tuple(map(int, key.split(',')))
    value = value.split(',')
    matrix = value[0]
    row, col, val = int(value[1]), int(value[2]), float(value[3])
  except:
    continue

  #If we are still on the same key...
  if key == current_key:
    
    #Process key/value pair
    if matrix == 'A':
      a_value, i_scale = StoreDataToA(matrix, row, col, a_value, i_scale)
    else:
      b_value, k_scale = StoreDataToB(matrix, row, col, b_value, k_scale)

  #Otherwise, if this is a new key...
  else:
    
    #If this is a new key and not the first key we've seen
    if current_key:
      
      #compute/output result to STDOUT
      CalculateElementMultiResult(current_key, a_value, b_value)

    current_key = key
    current_res = 0
    i_scale, k_scale = 0, 0
    a_value, b_value = dict(), dict()
    
    #Process input for new key
    if matrix == 'A':
      a_value, i_scale = StoreDataToA(matrix, row, col, a_value, i_scale)
    else:
      b_value, k_scale = StoreDataToB(matrix, row, col, b_value, k_scale)

#Compute/output result for the last key

if current_key:
  
  #compute/output result to STDOUT 
  CalculateElementMultiResult(current_key, a_value, b_value)


