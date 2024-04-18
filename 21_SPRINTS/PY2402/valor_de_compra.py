# -*- coding: utf-8 -*-
"""Valor de compra

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y16TlcWcjan2bpjXIinReQ8UsHDVFpSv
"""

valor_compra = float(input("Digite o valor da compra: R$ "))
num_prestacoes = int(input("Digite o número de prestações (1, 5, 12 ou 14): "))

def calcular_prestacoes(valor_compra, num_prestacoes):
    if num_prestacoes == 1:
        # À vista com 5% de desconto
        valor_prestacao = valor_compra * 0.95  # 5% de desconto
        print(f"Valor da prestação à vista: R$ {valor_prestacao:.2f}")
    elif num_prestacoes == 5:
        # 5x sem juros
        valor_prestacao = valor_compra / 5
        print(f"Valor de cada prestação em 5x sem juros: R$ {valor_prestacao:.2f}")
    elif num_prestacoes == 12:
        # 12x com juros de 12,4%
        taxa_juros = 0.124
        valor_prestacao = (valor_compra * (1 + taxa_juros)) / 12
        print(f"Valor de cada prestação em 12x com juros de 12,4%: R$ {valor_prestacao:.2f}")
    elif num_prestacoes == 14:
        # 14x com juros de 15,3%
        taxa_juros = 0.153
        valor_prestacao = (valor_compra * (1 + taxa_juros)) / 14
        print(f"Valor de cada prestação em 14x com juros de 15,3%: R$ {valor_prestacao:.2f}")
    else:
        print("Número de prestações não suportado. Tente 1, 5, 12 ou 14.")
calcular_prestacoes(valor_compra, num_prestacoes)