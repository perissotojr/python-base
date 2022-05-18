#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:
	export LANG=pt_BR

Execução:

	python3 hello.py
	ou
	./hello.py
"""
__version__ = "0.1.2"
__author__ = "Junior Perissoto" 
__license__ = "Unlicense"

#sets (Hash Table) - 0(1) - constante
#dicts (hash table)
import os

current_language = os.getenv("LANG" , "en_US")[:5]

msg = {
	"en_US": "Hello, World!",
	"pt_BR": "Olá, Mundo!",
	"it_IT": "Ciao, Mondo!",
	"es_SP": "Hola, Mundo!",
	"fr_FR": "Bonjour Monde",
}

#0(1) 
print(msg[current_language])