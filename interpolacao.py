#!/usr/bin/env python
""" Um exemplo como usar interpolação e placeholders no pyhton 
"""
__version__ = "0.0.1"
__author__ = "Junior Perissoto"


email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Esse produto é ótimo para resolver
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponiveis!

Preço promocional %(preco).2f
"""

clientes = ["Maria","Pedro","Jose"]

for cliente in clientes:
	print( 
	email_tmpl
	 %{
		"nome":cliente,
		"produto": "Caneta",
		"texto": "Escreve muito bem!!!",
		"link": "https://www.Canetaslegais.com",
		"quantidade": 1,
		"preco": 50.50,
	 })
