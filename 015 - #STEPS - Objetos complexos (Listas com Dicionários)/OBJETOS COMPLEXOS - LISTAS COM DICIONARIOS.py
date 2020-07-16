# LISTA
clientes = []

parar = 'n'

while parar != 's':
    print('### CADASTRO DE CLIENTES ### ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    cidade = input('Cidade: ')

    # Criando o objeto (dicionário) para colocar na lista.
    novo_cliente = {'detalhes': nome, 'idade': idade, 'cidade': cidade}
    clientes.append(novo_cliente)

    parar = input('PARAR [S ou N]: ')


print('DADOS DO CLIENTE >>>')
print('NOME: ', clientes[0]['nome'])
print('IDADE:', clientes[0]['idade'])
print('CIDADE:', clientes[0]['cidade'])


'''
Exemplo de um dicionário com listas 
filme = {
            'nome': 'Vingadores',
            'duracao': '3h',
            'idiomas': ['pt-br','eua','indi'],
            'generos': ['ficção', 'aventura' ,'drama']
         }

'''
