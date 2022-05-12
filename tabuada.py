#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

Tabuado do 1
1
2
3
....

------------------------------

Tabuada do 2
2
4
8
....

"""
__version__ = "0.1.0"
__author__ = "Junior Perissoto"


#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range(1, 11))

#leitura -> para cada numero me numeros:

for numero in numeros:
	print("Tabuada do:",numero)
	for outro_numero in numeros:
		print(numero * outro_numero)
	print("-----------------------")
