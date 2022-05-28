#!/usr/bin/env python
""" Imprime a mensagem de um email

NAO MANDE SPAM!!!
"""
__version__ = "0.1.0"
__author__ = "Junior Perissoto"

import os
import sys


argumentos = sys.argv[1:]

if not argumentos:
	print("Informe o nome do arquivo de emails")
	sys.exit(1)

filename = argumentos[0]
templatename = argumentos[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

clientes = []
for line in open(filepath):
	name , email = line.split(",")

	# TODO: subistituir ppor envio de email
	print(f"Enviando email para: {email}")
	print()
	print( 
	open(templatepath).read()
	 %{
		"nome":name,
		"produto": "Caneta",
		"texto": "Escreve muito bem!!!",
		"link": "https://www.Canetaslegais.com",
		"quantidade": 1,
		"preco": 50.50,
		"email": email,
	 })
	print("-" * 50)

