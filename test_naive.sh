#!/bin/bash

module load python/gnu/3.4.4

cat data/matsmall.txt | python src/naive_map.py 2 3 | sort -n | python src/naive_reduce.py 5
