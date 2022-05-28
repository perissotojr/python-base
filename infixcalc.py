#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
infixcalc.py sum 5 2
7

infixcalc.py mul 10 5
50

infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em infixcalc.log
"""
__version__ = "0.1.0"
 
import sys
import os

from datetime import datetime

argumentos = sys.argv[1:]

if not argumentos:
	operacao = input("Operação:")
	n1 = input("Digite número para n1:")
	n2 = input("Digite ńumero para n2:")
	argumentos = [operacao, n1 ,n2 ]
elif len(argumentos) !=3:
	print("Número de argumentos inválidos")
	print("ex: `sum 5 5`")
	sys.exit(1)

operacao, *nums =  argumentos

valida_operacoes = ("sum","sub","mul","div")
if operacao not in valida_operacoes:
	print("valida_operacoes")
	sys.exit(1)

num_validados = []
for num in nums:
	if not num.replace(".", "").isdigit():
		print(f"Número inválido {num}")
		sys.exit(1)
	if "." in num:
		num = float(num)
	else:
		num = int(num)
	num_validados.append(num)

n1 , n2 = num_validados

# TODO: usar dict de funcoes:
if operacao == "sum":
	resultado = n1 + n2
elif operacao == "sub":
	resultado = n1 - n2
elif operacao == "mul":
	resultado = n1 * n2
elif operacao == "div":
	resultado = n1 / n2	

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER','anonymous')

with open(filepath, "a") as file_:
	file_.write(f"{timestamp} - {user} - {operacao}, {n1} , {n2} = {resultado}\n")


print(f"O resultado é {resultado}")