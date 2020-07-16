# Criação da Lista:
pessoas = ['Rodrigo', 'Maria', 'Ana', 'Antonio']

# Adicionando um novo valor na lista:
nome = input('Informe a nova pessoa: ')
pessoas.append(nome)

# Exibindo o conteúdo da lista:
print('PESSOAS CADASTRADAS')
print(pessoas)

# Removendo o último valor da lista:
print('LISTA ATUALIZADA')
pessoas.pop()
print(pessoas)

# Removendo um item da lista pelo índice:
print('REMOVENDO UM INDICE ESPECIFICO')
pessoas.pop(0)
print(pessoas)

# Removendo um item da lista pelo conteúdo:
print('REMOVENDO O PRIMEIRO')
pessoas.remove('Rodrigo')
print(pessoas)


for item in pessoas:
    print(item)

