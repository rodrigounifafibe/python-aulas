"""
  > TASK 7:
  Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
  e mostre quantos Dólares ela pode comprar. Considere US$1.00 = R$4.10
"""

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.10

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
