# -*- Algoritimo e Linguagem de Programação -*-
"""
    Primeiros passos - Input e Output de dados
    Prof. Rodrigo Gonçalves Santana
"""

# Hello, World!
print('Hello, World! Com aspas simples')


'''
  Comentário com mais de uma linha!
'''

# Usando aspas.
print('É "Hello World!" que fala?')
print("É 'Hello World!' que fala?")


# Aspas simples ou dupla.
print("Hello, World! Com aspas duplas")

# Trabalhando com Variáveis (ainda sem saber o tipo).
mensagem = 'Hello, World! Armazenado em uma variável'
print(mensagem)

# Modificando o conteúdo de uma variável.
mensagem = 'Hello, World! Modificado...'
print(mensagem)

# Recebendo a mensagem de Hello World por input.
mensagem = input('Digite a mensagem: ')
print(mensagem)



# Pular linha com print sem parametro
print()


# Pular linha com \n
print('\n', mensagem)


# Concatenação de Valores

# 1 Concatenando com '+' e pulando linha com print vázio.
print()
print(mensagem + ' Enviado por input')

# 2 Concatenando e pulando linha com \n.
print('\nMensagem Enviada por input: ', mensagem)

# 3 Concatenando com Format.
print('{} > Mensagem enviada com input.'.format(mensagem))

# 4 Concatenando com Format simplificado
print(f'{mensagem}. *Enviada com input.')




### TASK 1
nome = input('Diga o seu nome: ')
print(f'Bem Vindo {nome}!')

### TASK 2
dia = input('Diga apenas o dia que você nasceu: ')
mes = input('Agora diga o mês que você nasceu: ')
ano = input('E por fim, diga o ano que você nasceu: ')
print(f'Você nasceu no dia {dia} de {mes} de {ano}. Correto?')