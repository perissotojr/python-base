#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---

	1X1 = 1
	1X2 = 2
	1X3 = 3
...
##########################################
---Tabuada do 2---

	2X1 = 2
	2X2 = 4
	2X3 = 6
...
##########################################
"""
__version__ = "0.1.1"
__author__ = "Junior Perissoto"

#alterações no codigo
#Iterable (percorriveis)

numeros = list(range(1, 11))

for num1 in numeros:
	print("{:-^20}".format(f"Tabuada do {num1}"))
	print()
	for num2 in numeros:
		resultado = num1 * num2
		print("{:^20}".format(f"{num1} X {num2} = {resultado}"))
	print("#" * 20)






