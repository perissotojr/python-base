#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:
	export LANG=pt_BR

Ou informe atraves do CLI argument '--lang'

Ou o usuario terá q digitar.
Execução:

	pyhthon3 nome_programa argumentos.

"""
__version__ = "0.1.3"
__author__ = "Junior Perissoto" 
__license__ = "Unlicense"

#sets (Hash Table) - 0(1) - constante
#dicts (hash table)
import os
import sys

#dicionario.
arguments ={"lang": None, "count": 1}

for arg in sys.argv[1:]:
	# TODO: Tratar ValueError 
	key,value =arg.split("=")
	key = key.lstrip("-").strip()
	value =  value.strip()
	if key not in arguments:
		print(f"Opção invalida {key}")
		sys.exit()
	arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
	# TODO: usar repetições
	if  "LANG" in os.environ:
		current_language = os.getenv("LANG")
	else:
		current_language = input("Escolha a linguagem:")

current_language = current_language[:5]

msg = {
	"en_US": "Hello, World!",
	"pt_BR": "Olá, Mundo!",
	"it_IT": "Ciao, Mondo!",
	"es_SP": "Hola, Mundo!",
	"fr_FR": "Bonjour Monde",
}

#0(1) 
print(msg[current_language] * int(arguments["count"]))