#!/usr/bin/python3.5

import sys
#sys.path.insert(0, '/home/elena/.local/lib/python3.5/')
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Prints out an nxn table')
parser.add_argument('-x', default=10)
parser.add_argument('-y', default=10)
args = parser.parse_args()

x = args.x
y = args.y

table = np.random.rand(x,y)

for i in range(x):
    for j in range(y):
        print("%.4f" %table[i][j],end="\t")
    print()
