# -*- coding: utf-8 -*-
"""for

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kcQj0jHw2qzQDpBTu5x2iains9HzSK6G
"""

a=int(input("Digite um número: "))

for b in [8,18,28,38,48,58,68,78,88]:
  if a==b:
    print("O número está na lista")
    break
else:
  print("O número não está na lista")