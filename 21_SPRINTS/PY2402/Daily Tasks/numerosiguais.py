# -*- coding: utf-8 -*-
"""numerosiguais.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qbsABxjTAJA29FaxF6ZsjLRq_uAiQOHm

Programa para verificar se dois números são iguais
"""

x,y=input('digite dois números:').split()

x=float(x)

y=float(y)

if x==y:
  print('Esses números são iguais')
else:
  print('Esses números não são iguais')