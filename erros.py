#!/bin/env python3
import sys
import os

#LBYL - look Before you leap.

#if os.path.exists("names.txt"):
#	print("o arquivo existe.")
#	input("...") #Race condition
#	names = open("names.txt").readlines()
#else:
#	print("[Error] File names.txt not found")
#	sys.exit(1)
#
#if len(names) >= 3:
#	print(names[2])
#else:
#	print("[Error:] Missing name in the list")
#	sys.exit(1)

###########################


#EAFP - "Easy to ASK forgiveness than permission"
# (é mais facil pedir perdao do que permissao.)


try:
	raise RuntimeError("Ocorreu um erro")
except Exception as e:
	print(str(e)) 

try:
	names = open("names.txt").readlines() 
	# FileNotFoundError
#	1 /1 #ZeroDivisionError
#	print(names.banana) # AttributeError
	
except FileNotFoundError as e:  		# except Bare execpt
	print(f"{str(e)}.")
	sys.exit(1)
	# TODO: USAR RETRY
else:
	print("Sucesso!!")	
finally:
	print("Excute isso sempre!!")

#except ZeroDivisionError:
#	print("[Error:] You cant divide by zero!!")
#	sys.exit(1)

#except AttributeError:
#	print("[Error:] List doesn't have banana") 
#	sys.exit(1)


try:
	print(names[2])
except:
	print("[Error:] Missing name in the list")
	sys.exit(1)