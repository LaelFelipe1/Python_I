# -*- coding: utf-8 -*-
"""wdeznumeros.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oLaG_wV_UzA5EkHmNxY0-9PQoJsxfNlL
"""

Programa para retornar o valor maior, menor e a média entre 10 valores digitados pelo usuário

maior=float(input('Digite um num:'))
menor=maior
soma=float()
qtdnum=9

while qtdnum>0:
  num=float(input('Digite um número'))
  if menor > num:
    menor=num
  if maior < num:
    maior=num
  soma=soma+num
  qtdnum=qtdnum-1


print('maior:',maior)
print('menor:',menor)
print('média:',soma/10)