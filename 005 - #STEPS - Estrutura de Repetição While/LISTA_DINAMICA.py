nomes = ['Ana', 'Maria', 'Antonio', 'Rodrigo']
parar = 'n'

while parar != 's':
    print('--- LISTA ---')
    print(nomes)

    posicao = int(input('Posição para remover: '))
    nomes.pop(posicao)
