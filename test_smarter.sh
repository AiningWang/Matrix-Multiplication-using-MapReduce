#!/bin/bash

module load python/gnu/3.4.4

cat data/matsmall.txt | python src/smarter_map.py 2 3 | sort -n | python src/smarter_reduce.py 5
