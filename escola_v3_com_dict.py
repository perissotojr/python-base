#!/usr/bin/env python3

"""Exibe relatorio de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequenta cada uma das
atividades.
"""
from pprint import pprint

__version__ = "0.3.0"
__author__ = "Junior Perissoto"

#melhando o codigo usando dicionarios:

salas = {
	"sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
	"sala2": ["Joao" , "Antonio" , "Carlos" ,"Maria", "Isolda"],
}

atividades = {
	"aula_ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
	"aula_musica":["Erik", "Carlos", "Maria"],
	"aula_danca":["Gustavo", "Sofia", "Joana", "Antonio"],
}

#Lista alunos atividade

# Listar alunos em cada atividade por sala.

for nome_atividade, atividade in atividades.items():

	print(f"Alunos da atividade {nome_atividade}")
	print("-" * 55)

	#Sala1 que tem interseção com a atividade
	atividade_sala1 = set(salas["sala1"]) & set(atividade)
	atividade_sala2 = set(salas["sala2"]) & set(atividade)

	print(f"{nome_atividade} sala1: ", atividade_sala1)
	print(f"{nome_atividade} sala2: ", atividade_sala2)
	print("")
	print("-" * 55)



