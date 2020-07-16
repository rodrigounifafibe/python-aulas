clientes = []

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    cidade = input('Cidade: ')
    saldo = float(input('Saldo atual: '))
    clientes.append({'nome': nome, 'idade': idade, 'cidade': cidade, 'saldo': saldo})
    print('LISTA DE CLIENTES --->')
    print(clientes)

    print('INFORMAÇÕES DO CLIENTE -->')

    print('Nome do cliente: ', clientes[0]['nome'])
    print('Cidade do cliente: ', clientes[0]['cidade'])
    print('Saldo do cliente: ', clientes[0]['saldo'])
