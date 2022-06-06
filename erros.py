#!/bin/env python3
import sys
import os

#LBYL - look Before you leap.

if os.path.exists("names.txt"):
	print("o arquivo existe.")
	input("...") #Race condition
	names = open("names.txt").readlines()
else:
	print("[Error] File names.txt not found")
	sys.exit(1)

if len(names) >= 3:
	print(names[2])
else:
	print("[Error:] Missing name in the list")
	sys.exit(1)

