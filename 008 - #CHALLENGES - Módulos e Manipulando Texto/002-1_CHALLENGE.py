# > DESAFIO 2 - PARTE 1
# Seu desafio é criar um programa que leia o nome completo do usuário. Em seguida, o seu programa mostrar:
#
#     -> Quantas letras o nome do usuário possui com e sem espaço.
#     -> Mostrar o nome do usuário com todas as letras minúsculas e maiúsculas.
#     -> Mostrar somente o primeiro nome.

nome = input('Informe o seu nome completo: ')

print('Algumas informações interessantes sobre o seu nome completo')
print()
print('Quantidade de Letras com espaço: ', len(nome))
print('Quantidade de Letras sem espaço: ', len(nome.replace(" ", "")))
print('Nome em minuscula:', nome.lower())
print('Nome em maiscula:', nome.upper())

# Uma maneira é gerar uma nova lista com cada palavra separada pelo caracter de espaço com o split e exibir a primeira palavra da lista com o índice 0.
lista = nome.split(" ")

print(lista[0])

# Outra maneira é exibir todos os caracteres desde do índice 0 até o primeiro caracter de espaço encontrado.
print(nome[0:nome.find(" ")])

