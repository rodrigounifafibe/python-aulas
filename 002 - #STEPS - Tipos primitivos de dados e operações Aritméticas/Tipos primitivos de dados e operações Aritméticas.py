# -*- Algoritimo e Linguagem de Programação -*-
"""
    Tipos primitivos de dados e operações Aritméticas
    Prof. Rodrigo Gonçalves Santana
"""

nome = input('Qual é o seu nome: ') 
print('Sextou! ' + nome + '. Borá tombar a nave!')
# Pula de linha
print()
curso = input('Qual curso você faz? ')
# Primeira forma de concatenar valores com sinal de +
print('O curso ' + curso + 'é bem legal! ')
# Segunda forma de concatenar com a vírgula
print('O curso ', curso, ' é bem legal! ')
# Terceira forma de concatenar com {} format.
print('O curso {} é bem legal {}! '.format(curso, nome))
# Quarta forma de concatenar com format
print(f'O curso {curso} é legal {nome}!')

# Task 1 da aula 07/02
usuario = input('Digite o seu nome: ')
print(f'Boa noite {usuario}. Feliz por você estar aqui!')

# Task 2 da aula 07/02
dia = input('Que dia você nasceu?')
mes = input('Agora, me diga o mês?')
ano = input('Finalmente, qual ano você nasceu?')

print(f'Você nasceu no dia {dia} de {mes} do ano {ano}. Certo?')

# Trabalhando com Tipos de Dados
valor = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é: ', type(valor))
print()
# Funções de verificação de String
print('Esse texto tem espaços? ', valor.isspace())
print('É número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanúmerico?', valor.isalnum())
print('Está em maiúscula?', valor.isupper())
print('Está em minúscula?', valor.islower())  
print('A primeira letra é maiúscula?', valor.istitle())

valor = int(input('Informe um número inteiro: '))
print('Tipo do valor: ', type(valor))
print()
valor = float(input('Informe um número float:'))
print('Tipo do valor: ', type(valor))
print()
valor = bool(input('Diga TRUE para sim ou FALSE para não: '))
#Interpolação de String
print(f'O valor {valor } é do tipo {type(valor)}')

# Operações Aritméticas
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
print(f'O resultado da soma é {v1 + v2}')
print(f'O resultado da subtração é {v1 - v2}')
print(f'O resultado da multiplicação é {v1 * v2}')
print(f'O resultado da divisão é {v1 / v2}')
print(f'O resultado da potência: {v1 ** v2}')