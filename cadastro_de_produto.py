#!/user/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"
__author__ = "Junior Perissoto"

#import pprint
from pprint import pprint

#variaveis "comum"

#produto_nome = "Caneta"
#produto_cor1 = "azul"
#produto_cor2 = "branco"
#produto_preco = 3.23
#produto_dimensao_altura = 12.1
#produto_dimensao_largura = 0.8
#produto_em_estoque = True
#produto_codigo = 45678
#produto_codebar = None

# com dicionario:

produto = {
	"nome": "Caneta",
	"cores": ["azul","branco"],
	"preco": 3.23,
	"dimensao": {
		"altura": 12.1,
		"largura": 0.8,
	},
	"em_estoque":True,
	"codigo": 45678,
	"codebar": None,
}

#melhorando o codigo usando dicionarios:

cliente ={
	"nome": "Junior"
}

compra = {
	"cliente": cliente,
	"produto": produto,
	"quantidade": 3,
}

#pprint(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
	 f"O cliente {compra['cliente']['nome']}" 
	 f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
	 f" e pagou o total de: {total_compra}")