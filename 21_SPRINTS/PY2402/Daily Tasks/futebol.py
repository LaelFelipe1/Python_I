# -*- coding: utf-8 -*-
"""Futebol

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17ULr00Vo8Ez84_cZS91RSVv4fO3kcOJ9
"""

RealMadrid = int(input("Quantos gols Real Madrid fez? "))
Barcelona = int(input("Quantos gols Barcelona fez? "))

GolsTotal = (RealMadrid + Barcelona)
print(GolsTotal)

if RealMadrid == Barcelona :
  print("Empate.")

if RealMadrid > Barcelona :
  print("Real Madrid ganhou!")
else :
  print("Real Madrid perdeu!")

if Barcelona > RealMadrid :
  print("Barcelona ganhou!")
else :
  print("Barcelona perdeu!")