# -*- coding: utf-8 -*-
"""jurosimples.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13s-K2kVhlerPEhVi1RE-UACSd9Zov4sR

Cálculo de juros simples
"""

c=float(input('digite o valor inicial pago/a pagar:'))

n=float(input('digite o núm de dias em que o juros estão ocorrendo:'))

i=float(input('digite o percentual de juros incididos somente em digitos (expl. 15% = 15):'))

total = c+(c*n*(i/100))

print('o valor total é:', total)