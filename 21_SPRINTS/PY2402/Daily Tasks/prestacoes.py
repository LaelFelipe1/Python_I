# -*- coding: utf-8 -*-
"""prestacoes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1loUJ-uG79nwCEifwU5ylJvaB37o7UVfB

Programa para dizer a quantidade de juros pagos de acordo com o numero de prestações digitadas
"""

p=float(input('digite o valor do produto:'))

n=input('digite o quantas prestações iá pagar: \nopções:\n\nà vista: 5% de desconto\n5 vezes: 5% de juros\n12 vezes: 12,4% de juros\n14 vezes: 15,3% de juros\ndigite aqui:')

if n.isnumeric()==False:
  print('Você escolheu pagamento à vista. Você recebeu 5% de desconto! O valor total a pagar agora é: {:.2f}'.format(p*0.05-p))
else:
  n=float(n)

def montante (i):
  x=(p*i+p)
  return(x)

if n == 5:
  i=0.05
elif n==12:
  i=0.124
elif n==14:
  i=0.153

print(\
'Você escolheu seu pagamento em {:.0f} vezes.\n\
Os juros mensais a pagar são de {:.1f}%.\n\
Serão {:.0f} parcelas de:{:.2f}\n\
total final da compra:{:.2f}\n\
diferença total:R$:{:.2f} a uma diferença mensal de R$:{:.2f}'\
\
.format(n,i*100,n,montante(i)/n,montante(i),montante(i)-p,(montante(i)/n)-p/n))