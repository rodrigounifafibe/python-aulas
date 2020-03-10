""" 
  > TASK 2:
  Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('De acordo com o numero {}, seu antecessor é {} e o sucessor é {}'.format(numero, antecessor, sucessor))
# Utilizando apenas um variavael
print('De acordo com o numero {}, seu antecessor é {} e o sucessor é {}'.format(numero, (numero - 1), (numero + 2)))
